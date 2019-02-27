"""
models.py  
- Data classes for the surveyapi application
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Sheet(db.Model):
    __tablename__ = 'sheets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    chords = db.relationship('Chord', backref="sheet",
                             cascade="all, delete-orphan", lazy=False)
    navIsOpen = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return dict(id=self.id,
                    name=self.name,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    chords=[chord.to_dict() for chord in self.chords],
                    navIsOpen=self.navIsOpen)


class Chord(db.Model):
    __tablename__ = 'chords'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(2), nullable=False)
    notes = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=None)
    sheet_id = db.Column(db.Integer, db.ForeignKey(
        'sheets.id', ondelete='CASCADE'))
    inversions = db.relationship('Inversion', backref='chord', lazy=False)

    def to_dict(self):
        return dict(id=self.id,
                    name=self.name,
                    notes=self.notes,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    updated_at=self.updated_at.strftime(
                        '%Y-%m-%d %H:%M:%S') if self.updated_at != None else None,
                    sheet_id=self.sheet_id,
                    inversions=[inversion.to_dict() for inversion in self.inversions])


class Inversion(db.Model):
    __tablename__ = 'inversions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    chord_id = db.Column(db.Integer, db.ForeignKey('chords.id'))

    def to_dict(self):
        return dict(id=self.id,
                    name=self.name,
                    notes=self.notes,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    chord_id=self.chord_id)
