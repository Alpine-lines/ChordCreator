"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request
from .models import db, Sheet, Chord, Inversion
from packages.chord_sheets import major, minor, inversions
from datetime import datetime

api = Blueprint('api', __name__)


@api.route('/sheets/', methods=('GET', 'POST'))
def sheets():
    if request.method == 'GET':
        sheets = Sheet.query.all()
        return jsonify({'sheets': [s.to_dict() for s in sheets]})
    elif request.method == 'POST':
        data = request.json
        sheet = Sheet(name=data['name'])
        chords = []
        for c in data['chords']:
            root_note = c['root']
            chord = Chord(root=root_note)
            chord.major = major(root_note)
            chord.minor = minor(root_note)
            chord.inversions = [Inversion(name=str(i), notes=notes)
                                for i, notes in enumerate(inversions(root_note))]
            chords.append(chord)
        sheet.chords = chords
        db.session.add(sheet)
        db.session.commit()
        return jsonify(sheet.to_dict()), 201


@api.route('/sheets/<int:sheetId>/', methods=('GET', 'PUT', 'DELETE'))
def sheet(sheetId):
    if request.method == 'GET':
        sheet = Sheet.query.get(sheetId)
        return jsonify({'sheet': sheet.to_dict()})
    elif request.method == 'PUT':
        data = request.json
        root_note = data['root']
        chord = Chord(root=root_note, sheet_id=sheetId)
        chord.root = root_note
        chord.major = major(root_note)
        chord.minor = minor(root_note)
        chord.inversions = [Inversion(name=str(i), notes=notes)
                            for i, notes in enumerate(inversions(root_note))]
        db.session.add(chord)
        db.session.commit()
        return jsonify(chord.to_dict()), 201
    elif request.method == 'DELETE':
        db.session.query(Sheet).filter(Sheet.id == sheetId).delete()
        db.session.commit()
        return jsonify({"msg": f"Sheet {sheetId} has been deleted."}), 201


@api.route('/sheets/<int:sheetId>/<int:chordId>/', methods=('GET', 'PUT', 'DELETE'))
def chord(sheetId, chordId):
    if request.method == 'GET':
        chord = db.session.query(Chord).join(Sheet).filter(
            Sheet.id == sheetId).filter(Chord.id == chordId).first()
        return jsonify(chord.to_dict())
    elif request.method == 'PUT':
        data = request.json
        chord = db.session.query(Chord).join(Sheet).filter(
            Sheet.id == sheetId).filter(Chord.id == chordId).first()
        root_note = data['root']
        chord.root = root_note
        chord.major = major(root_note)
        chord.minor = minor(root_note)
        chord.inversions = [Inversion(name=str(i), notes=notes)
                            for i, notes in enumerate(inversions(root_note))]
        db.session.commit()
        return jsonify(chord.to_dict()), 201
    elif request.method == 'DELETE':
        db.session.query(Chord).filter(
            Chord.sheet_id == sheetId).filter(Chord.id == chordId).delete()
        db.session.commit()
        return jsonify({"msg": f"Chord {chordId} has been deleted from Sheet {sheetId}."}), 201


@api.route('/sheets/<int:sheetId>/<int:chordId>/<int:inversionId/')
def get_inversion(sheetId, chordId, inversionId):
    inversion = db.session.query(Inversion).join(Chord).join(
        Sheet).filter(Chord.id == chordId).filter(Sheet.id == sheetId).filter(
            Inversion.id == inversionId).first()
    return jsonify({"inversion": inversion.to_dict()})
