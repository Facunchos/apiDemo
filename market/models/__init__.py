# models/__init__.py
from .user import User
from .item import Item
from .ability import Ability
from .stat import Stat

from market import db, login_manager
from market import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

__all__ = ['User', 'Item', 'Ability', 'Stat']
