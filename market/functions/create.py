from market import app
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User, Stat, Ability
from market.forms import (
    RegisterForm,
    LoginForm,
    PurchaseItemForm,
    SellItemForm,
    ItemCreateForm,
    StatCreateForm,
)
from market import db
from flask_login import login_user, logout_user, login_required, current_user


def item_create_page():
    form = ItemCreateForm()
    if form.validate_on_submit():
        item_to_create = Item(
            name=form.name.data,
            price=form.price.data,
            barcode=form.barcode.data,
            description=form.description.data,
        )
        db.session.add(item_to_create)
        db.session.commit()
        flash(
            f"Item created successfully!",
            category="success",
        )
        return redirect(url_for("market_page"))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(
                f"There was an error with creating a Item: {err_msg}", category="danger"
            )

    return render_template("/forms/item_create.html", form=form)

def stat_create_page():
    form = StatCreateForm()
    if form.validate_on_submit():
        stat_to_create = Stat(
            name=form.name.data,
        )
        db.session.add(stat_to_create)
        db.session.commit()
        flash(
            f"Stat created successfully!",
            category="success",
        )
        return redirect(url_for("market_page"))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(
                f"There was an error with creating the Stat: {err_msg}", category="danger"
            )

    return render_template("/forms/stat_create.html", form=form)