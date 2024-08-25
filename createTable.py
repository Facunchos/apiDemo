from market import db
db.create_all()
from market.models import Ability
new_table = Ability(name='Fuerza', level=1)
db.session.add(new_table)
db.session.commit()