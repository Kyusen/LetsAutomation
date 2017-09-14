# -*- coding: utf-8 -*-
__author__ = "Leonardo Otacílio Narciso Ramos"

from flask_login import LoginManager
login_manager = LoginManager()

from flask.exthook import ExtDeprecationWarning
import warnings

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

warnings.simplefilter('ignore', ExtDeprecationWarning)
warnings.simplefilter("ignore", UserWarning)
