# -*- coding: utf-8 -*-
'''
    The models are here
'''
__author__ = "Leonardo Otacílio Narciso Ramos"

from sqlalchemy import or_
from passlib.apps import custom_app_context as pwd_context
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import exists
from datetime import datetime, timedelta
from sqlalchemy import Column
from sqlalchemy.orm import synonym
from sqlalchemy.types import *
from config.extensions import db


class User(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    login = Column(String(32), index=True, unique=True, nullable=False)
    email = Column(String(128), index=True, unique=True, nullable=False)
    created_on = Column(DateTime, nullable=False, default=datetime.now())
    _password = Column('password', String(128), nullable=False)

    # Required for administrative interface
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __unicode__(self):
        return self.login

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = generate_password_hash(password)

    password = synonym('_password',
                       descriptor=property(_get_password,
                                           _set_password))

    def __init__(self, first_name, last_name, login, email, _password):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.email = email
        self._password = generate_password_hash(_password)

    def check_password(self, password):
        if self.password is None:
            return False
        return check_password_hash(self.password, password)

    def hash_password(self, password):

        self._password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self._password)

    @classmethod
    def authenticate(cls, login, password):
        user = db.session.query(User).filter(or_(User.login == login)).first()

        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False
        return user, authenticated

    @classmethod
    def is_user_name_taken(cls, login):
        return db.session.query(exists().where(User.login == login)).scalar()

    @classmethod
    def is_email_taken(cls, email_address):
        return db.session.query(exists().where(User.email == email_address)).scalar()

    def serialize(self):
        return {'id': self.id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'login': self.login,
                'email': self.email,
                'created_on': self.created_on
                }
