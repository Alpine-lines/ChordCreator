"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request
from .models import db, Sheet, Chord, Inversion
from packages.chord_sheets import major, minor, inversions

api = Blueprint('api', __name__)


@api.route('/hello/<string:name>/')
def say_hello(name):
    response = {'msg': "Hello {}".format(name)}
    return jsonify(response)


@api.route('/sheets/')
def get_sheets():
    sheets = Sheet.query.all()
    return jsonify({'sheets': [s.to_dict() for s in sheets]}),


@api.route('/sheets/<int:id>/')
def get_sheet(id):
    sheet = Sheet.query.get(id)
    return jsonify({'sheet': sheet.to_dict()})


@api.route('/new-sheet/', methods=('POST'))
def new_sheet():
    if request.method == 'POST':
        data = request.json()
        sheet = Sheet(name=data['name'])
        chords = []
        for c in data['chords']:
            root_note = c['root']
            chord = Chord(root=root_note)
            chord.major = major = major(root_note)
            chord.minor = minor(root_note)
            inversion_list = inversions(c['root'])
            chord.inversions = [Inversion(name=str(inversion_list.index(
                i)), notes=(i)) for i in inversion_list]
            chords.append(chord)
        sheet.chords = chords
        db.session.add(sheet)
        db.session.commit()
        return jsonify(sheet.to_dict()), 201
