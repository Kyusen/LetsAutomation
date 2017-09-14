# -*- coding: utf-8 -*-
__author__ = 'Leonardo Otacílio Narciso Ramos'

from model.model import *


def create_initial_dataset():
    try:
        data_task = {'first_name': 'admin',
                     'last_name': 'admin',
                     'login': 'admin',
                     'email': 'admin@example.com',
                     '_password': 'admin'}

        create_data = User(**data_task)

        db.session.add(create_data)
        db.session.commit()

    except Exception as e:
        print(e)
        db.session.rollback()
