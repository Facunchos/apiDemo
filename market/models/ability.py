
from market import db


class Ability(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    stat_id = db.Column(db.Integer(), db.ForeignKey('stat.id'), nullable=False, default=1)
    level = db.Column(db.Integer(), nullable=True, default=0)
    description = db.Column(db.String(length=1024), nullable=False, unique=True, default='')
    bonus_t = db.Column(db.Integer(), nullable=True, default=0)
    bonus_k = db.Column(db.Integer(), nullable=True, default=0)
    bonus_sum = db.Column(db.Integer(), nullable=True, default=0)
    expertise = db.Column(db.Boolean(), nullable=True, default=False)

    def __init__(self, name, stat_id, level, description, bonus_t, bonus_k, bonus_sum, expertise):
        self.name = name
        self.stat_id = stat_id
        self.level = level
        self.description = description
        self.bonus_t = bonus_t
        self.bonus_k = bonus_k
        self.bonus_sum = bonus_sum
        self.expertise = expertise
    


    def dice(self, character):
        dice = self.bonus_t + character.stats[self.stat_id].value + self.level
        dice_k = self.bonus_k + character.stats[self.stat_id].value + self.level
        return f"{dice}K{dice_k} + {self.bonus_sum}"
    
    
    def __repr__(self):
        return f'Ability: {self.name}'