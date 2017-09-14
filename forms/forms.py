# -*- coding: utf-8 -*-
__author__ = "Leonardo Otacílio Narciso Ramos"

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):

    login = StringField('login', validators=[DataRequired()], render_kw={"placeholder": 'username'})
    password = PasswordField('password', validators=[DataRequired()], render_kw={"placeholder": 'password'})
