"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request
from .models import db, Sheet, Chord, Inversion
from music21 import *
from mingus.core import chords as ch
from datetime import datetime as dt

api = Blueprint('api', __name__)


@api.route('/test/')
def test():
    return jsonify({"C": ch.from_shorthand("C")})


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
            shorthand_notation = c['name']
            chord = Chord(name=shorthand_notation)
            chord.notes = ' '.join(ch.from_shorthand(shorthand_notation))
            print(chord.notes)
            inversions = [' '.join(ch.first_inversion(chord.notes.split(' '))),
                          ' '.join(ch.second_inversion(
                              chord.notes.split(' '))),
                          ' '.join(ch.third_inversion(chord.notes.split(' ')))]
            chord.inversions = [Inversion(name=str(i), notes=notes)
                                for i, notes in enumerate(inversions)]
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
        shorthand_notation = data['name']
        chord = Chord(name=shorthand_notation, sheet_id=sheetId)
        chord.name = shorthand_notation
        chord.notes = ' '.join(ch.from_shorthand(shorthand_notation))
        inversions = [' '.join(ch.first_inversion(chord.notes.split(' '))),
                      ' '.join(ch.second_inversion(
                          chord.notes.split(' '))),
                      ' '.join(ch.third_inversion(chord.notes.split(' ')))]
        chord.inversions = [Inversion(name=str(i), notes=notes)
                            for i, notes in enumerate(inversions)]
        chord.updated_at = dt.utcnow()
        db.session.add(chord)
        db.session.commit()
        return jsonify(chord.to_dict()), 201
    elif request.method == 'DELETE':
        chordIds = [chord.id for chord in db.session.query(Chord).join(
            Sheet).filter(Sheet.id == sheetId).all()]
        db.session.query(Sheet).filter(Sheet.id == sheetId).delete()
        for id in chordIds:
            db.session.query(Chord).filter(
                Chord.sheet_id == sheetId).filter(Chord.id == id).delete()
            db.session.query(Inversion).filter(
                Inversion.chord_id == id).delete()
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
        shorthand_notation = data['name']
        chord.name = shorthand_notation
        chord.notes = ' '.join(ch.from_shorthand(shorthand_notation))
        inversions = [' '.join(ch.first_inversion(chord.notes.split(' '))),
                      ' '.join(ch.second_inversion(
                          chord.notes.split(' '))),
                      ' '.join(ch.third_inversion(chord.notes.split(' ')))]
        chord.inversions = [Inversion(name=str(i), notes=notes)
                            for i, notes in enumerate(inversions)]
        chord.updated_at = dt.utcnow()
        db.session.commit()
        return jsonify(chord.to_dict()), 201
    elif request.method == 'DELETE':
        db.session.query(Chord).filter(
            Chord.sheet_id == sheetId).filter(Chord.id == chordId).delete()
        db.session.query(Inversion).filter(
            Inversion.chord_id == chordId).delete()
        db.session.commit()
        return jsonify({"msg": f"Chord {chordId} has been deleted from Sheet {sheetId}."}), 201


@api.route('/sheets/<int:sheetId>/<int:chordId>/<int:inversionId>/')
def get_inversion(sheetId, chordId, inversionId):
    inversion = db.session.query(Inversion).join(Chord).join(
        Sheet).filter(Chord.id == chordId).filter(Sheet.id == sheetId).filter(
            Inversion.id == inversionId).first()
    return jsonify({"inversion": inversion.to_dict()})
