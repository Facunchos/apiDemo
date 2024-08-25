from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User, Item, Stat

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')
    
class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField('Purchase Item!')
    # This is a button that will be used to purchase the item

class SellItemForm(FlaskForm):
    submit = SubmitField('Sell Item!')

class ItemCreateForm(FlaskForm):
    name = StringField(label='Name:', validators=[Length(min=2, max=30), DataRequired()])
    price = StringField(label='Price:', validators=[DataRequired()])
    barcode = StringField(label='Barcode:', validators=[Length(min=12, max=12), DataRequired()])
    description = StringField(label='Description:', validators=[DataRequired()])
    submit = SubmitField(label='Add Item!')
    
    def validate_barcode(self, barcode_to_check):
        barcode = Item.query.filter_by(barcode=barcode_to_check.data).first()
        if barcode:
            raise ValidationError('Barcode already exists! Please try a different barcode')
        
    def validate_name(self, name_to_check):
        name = Item.query.filter_by(name=name_to_check.data).first()
        if name:
            raise ValidationError('Item name already exists! Please try a different name')
       
class StatCreateForm(FlaskForm):
    name = StringField(label='Name:', validators=[Length(min=2, max=30), DataRequired()])
    submit = SubmitField(label='Add Stat!')
    
    def validate_name(self, name_to_check):
        name = Stat.query.filter_by(name=name_to_check.data).first()
        if name:
            raise ValidationError('Stat already exists! Please try a different name')