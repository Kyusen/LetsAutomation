# -*- coding: utf-8 -*-
'''
 LetsAutomation Documentation
    :platform: Unix
    :synopsis: init app
'''

__author__ = "Leonardo Otacílio Narciso Ramos"
__copyright__ = "Copyright 2017, The automate residence"
__credits__ = ["Vinicius"]

__maintainer__ = "Leonardo Otacílio Narciso Ramos"
__email__ = "leonardo.nramos@gmail.com"

from flask import Flask
from config.extensions import db, login_manager
from flask_cors import CORS
from model import initial_dataset
from auth import login
from webaspio import webraspio


def build_app():
    '''
        Initialization the app and setting the configs
        Args:
            None

        :return: This funcion set the configs to init app
    '''

    app = Flask(__name__, static_folder='../static', template_folder='../templates')

    app.config.from_object('config.config.GeneralConfig')

    CORS(app, resources=r'/*', allow_headers='Content-Type')

    db.app = app

    db.init_app(app)

    login_manager.init_app(app)

    init_config(app)

    return app


def init_config(app):
    """Choose the config to load the project

    :param app:
    :return: Function conf to choose in load app
    """

    setup_app(app)


def setup_app(app):
    """Only show in the console the enviroment choose

    :param app:
    :return: enviroment
    """

    app.register_blueprint(login.login_service, url_prefix='/auth')
    app.register_blueprint(webraspio.web, url_prefix='/webaspio')

    db.create_all()
    initial_dataset.create_initial_dataset()

    environment = app.config['AMBIENTE']
    print('Executando aplicacao no ambiente: {}'.format(environment))


app = build_app()


if __name__ == "__main__":
    app.run(port=app.config['PORT'],
            debug=app.config['DEBUG'])


