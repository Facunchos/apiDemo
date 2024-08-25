
from market import db


class Ability(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    stat_id = db.Column(db.Integer(), db.ForeignKey('stat.id'), nullable=False)
    level = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    bonus_t = db.Column(db.Integer(), nullable=False)
    bonus_k = db.Column(db.Integer(), nullable=False)
    bonus_sum = db.Column(db.Integer(), nullable=False)
    expertise = db.Column(db.Boolean(), nullable=False, default=False)

    def dice(self, character):
        dice = self.bonus_t + character.stats[self.stat_id].value + self.level
        dice_k = self.bonus_k + character.stats[self.stat_id].value + self.level
        return f"{dice}K{dice_k} + {self.bonus_sum}"
    
    
    def __repr__(self):
        return f'Ability: {self.name}'