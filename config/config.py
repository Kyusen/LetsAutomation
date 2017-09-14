# -*- coding: utf-8 -*-
'''
    This file contain all important configuration about this project
'''

__author__ = "Leonardo Otacílio Narciso Ramos"
__copyright__ = "Copyright 2017, The automate residence"
__credits__ = ["Vinicius"]

__maintainer__ = "Leonardo Otacílio Narciso Ramos"
__email__ = "leonardo.nramos@gmail.com"

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DatabaseConfig(object):
    '''
        All configs are in this class
    '''

    SECRET_KEY = '91a45718-20a4-4fc5-8116-ef3f375a30d6'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_POOL_SIZE = 10
    #SQLALCHEMY_MAX_OVERFLOW = 10
    #SQLALCHEMY_POOL_RECYCLE = 60
    #WTF_CSRF_ENABLED = True
    DATABASE_NAME = 'lets_automation.sqlite'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, DATABASE_NAME)


class GeneralConfig(DatabaseConfig):

    AMBIENTE = 'Local'
    DEBUG = True
    PORT = 5000
    BASE = 'http://127.0.0.1:' + str(PORT)



