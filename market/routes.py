from market import app
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from market.functions import create, base_page


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/market", methods=["GET", "POST"])
@login_required
def market_page():
    return base_page.market_page()

@app.route("/register", methods=["GET", "POST"])
def register_page():
    return base_page.register_page()


@app.route("/login", methods=["GET", "POST"])
def login_page():
    return base_page.login_page()


@app.route("/logout")
def logout_page():
   return base_page.logout_page()


@app.route("/forms/item_create", methods=["GET", "POST"])
def item_create_page():
    return create.item_create_page()

@app.route("/forms/stat_create", methods=["GET", "POST"])
def stat_create_page():
    return create.stat_create_page()