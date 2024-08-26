
from market import db

class Stat(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    level = db.Column(db.Integer(), nullable=False, default=0)

    abilities = db.relationship('Ability', backref='stat', lazy=True)
    
    def __repr__(self):
        return f'Stat: {self.name}'