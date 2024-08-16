Set the pc to run that project like main file

$export FLASK_APP=market.py
$flask run

For refreshing after savefile
$export FLASK_DEBUG=1

We are using Bootstrap 4.5. Later change it to 5.0


Intalls: 
pip3 install flask-sqlalchemy
pip3 install flask-wtf
pip3 install wtforms
pip install email_validator
pip install flask_bcrypt
pip install flask_login
--

python3
>>> from market import db
>>> db.create_all()
>>> from market import Item
>>> item1 = Item(name="Iphone 10", price=500, barcode='151515', description='An Iphone 10')
>>> db.session.add(item1)
>>> db.session.commit()

>>> Item.query.all()
[<Item 1>]
>>> item2 = Item(name='Laptop', price=600, description='an Lapton gg', barcode='15515643')
>>> db.session.add(item2)
>>> db.session.commit()
>>> Item.query.all()
[<Item 1>, <Item 2>]

>>> from market import db
>>> from market import Item
>>> Item.query.all()

Item.query.filter_by(price=600)

---

>>> db.session.rollback()
>>> item1.owner = User.query.filter_by(username='asd').first().id
>>> item1.owner
1
>>> db.session.add(item1)
>>> db.session.commit()
>>> item1.owner
1
>>> i = Item.query.flter_by(name='telefono')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'BaseQuery' object has no attribute 'flter_by'
>>> i = Item.query.filter_by(name='telefono')
>>> i = Item.query.filter_by(name='telefono').first()
>>> i.owned_user
<User 1>
>>> 
