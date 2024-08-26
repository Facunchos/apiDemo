from market import db
db.create_all()
from market.models import Ability
new_table = Ability(name='Mano a Mano', level=0, stat_id=1, description='Peleas en Bar', bonus_t=0, bonus_k=0, bonus_sum=0, expertise=False)
db.session.add(new_table)
db.session.commit()