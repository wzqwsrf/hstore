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


def get_user_keys():
    session = get_session_not_commit()
    with session.begin(subtransactions=True):
        return session.query(UserHstore.info).filter(UserHstore.info.keys()).all()


def user_contains_key_value(key, value):
    session = get_session_not_commit()
    with session.begin(subtransactions=True):
        return session.query(UserHstore).filter(UserHstore.info.contains({key: value})).one()


def user_constains_key(key):
    session = get_session_not_commit()
    with session.begin(subtransactions=True):
        user = session.query(UserHstore).filter(UserHstore.info.has_key(key)).first()
        if user:
            return True
        return False


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
        session.query(UserHstore).filter(UserHstore.info['name'] == name).update(
            {UserHstore.info: UserHstore.info + {key: value, }, },
            synchronize_session="fetch")


def del_user_by_key(key1, key2):
    session = get_session()
    with session.begin(subtransactions=True):
        for user in session.query(UserHstore).filter(UserHstore.info.has_key(key1)):
            del user.info[key2]




