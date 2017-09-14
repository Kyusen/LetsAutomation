# -*- coding: utf-8 -*-
__author__ = "Leonardo Otacílio Narciso Ramos"

from flask import (flash, session, Blueprint, render_template,
                   redirect, url_for, request, g, current_app)
from flask_login import login_user, logout_user
from functools import wraps
from sqlalchemy.sql.functions import current_user
from config.extensions import login_manager
from forms.forms import LoginForm
from model.model import *


login_service = Blueprint('login_service', __name__)


@login_manager.unauthorized_handler
def unauthorized():
    '''Return for screen to login'''
    return redirect(url_for('login_service.login', next=request.url))


def login_required(f):
    '''Verify user is logged if not return for screen to login'''
    @wraps(f)
    def decorated_function(*args, **kwargs):
        expires_in = session.get('expires_in', None)
        if expires_in is None:
            return redirect(url_for('login_service.login', next=request.url))
        else:
            if not isinstance(expires_in, datetime):
                session.clear()
            if 'user_id' not in session.keys() or datetime.now() > expires_in:
                session.clear()
                return redirect(url_for('login_service.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@login_manager.user_loader
def load_user(user_id):
    '''
        load user if logged
    '''
    return db.session.query(User).get(user_id)


@login_service.route('/', methods=['GET', 'POST'])
@login_service.route('/login', methods=['GET', 'POST'])
def login():
    '''
        Function login, load screen to login and verify
        the form is filled and user and password is valid
    '''

    form = LoginForm()

    try:
        if session['logged_in']:
            return redirect(url_for('publisher.home'))
    except Exception as e:
        pass

    if form.validate_on_submit():

        user = db.session.query(User).filter_by(login=form.login.data).first()

        if user is None:
            message = "Usuário ou Senha Inválidos"
            flash(message)
            return redirect(url_for('login_service.login', next=request.url))

        if check_password_hash(user._password, form.password.data):

            login_user(user)
            session['logged_in'] = True

            next = request.args.get('next', '')

            return redirect(next or url_for('web.home'))

    return render_template('login.html',
                           form=form)


@login_service.route('/logout', methods=['GET'])
@login_required
def logout():
    '''
        logout user
    '''
    session.pop('login', None)
    logout_user()
    session.clear()
    return redirect(url_for('login_service.login'))


@login_service.before_request
def before_request():
    '''
        get user name
    '''
    g.user = current_user


@login_service.before_request
def make_session_permanent():
    '''
        Define time to user session is logged
    '''
    session.permanent = True
    current_app.permanent_session_lifetime = timedelta(minutes=60)
    session['expires_in'] = datetime.now() + timedelta(hours=3)


def get_user():
    '''
        Return user login
    '''
    user = db.session.query(User).filter_by(id=session['user_id']).first()
    return user.login


def get_user_id():
    '''
        Return user id
    '''
    user = db.session.query(User).filter_by(id=session['user_id']).first()
    return user.id