# !/usr/bin/env python
# -*- coding: utf-8 -*-
from pyhstore.db.db_connect import get_session, get_session_not_commit
from pyhstore.models.user_hstore import UserHstore


def add_user(info):
    session = get_session()
    with session.begin(subtransactions=True):
        userHstore = UserHstore()
        userHstore.info = info
        session.add(userHstore)


def get_user_all():
    session = get_session_not_commit()
    with session.begin(subtransactions=True):
        return session.query(UserHstore).all()


def get_user_by_key(key):
    session = get_session_not_commit()
    with session.begin(subtransactions=True):
        return session.query(UserHstore).filter(UserHstore.info.has_key(key)).first()


def get_user_by_key_equal_value(key, value):
    session = get_session_not_commit()
    with session.begin(subtransactions=True):
        return session.query(UserHstore).filter(UserHstore.info[key] == value).first()


def edit_user_by_key_value(key, value1, value2):
    session = get_session()
    with session.begin(subtransactions=True):
        userHstore = session.query(UserHstore).filter(UserHstore.info[key] == value1).first()
        userHstore.info[key] = value2
        session.add(userHstore)


def add_user_new_key_value_by_name(key, value, name):
    session = get_session()
    with session.begin(subtransactions=True):
        userHstore = session.query(UserHstore).filter(UserHstore.info['name'] == name).first()
        info = userHstore.info
        info[key] = value
        userHstore.info = info
        session.add(userHstore)


def del_user_key_value_by_name(key, value, name):
    session = get_session()
    with session.begin(subtransactions=True):
        userHstore = session.query(UserHstore).filter(UserHstore.info['name'] == name).first()
        info = userHstore.info
        info[key] = value
        userHstore.info = info
        session.add(userHstore)




