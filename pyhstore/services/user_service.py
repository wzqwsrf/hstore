# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2014年12月09日16:25:23
# Auther: wangzhenqing(wangzhenqing1008@163.com)

from pyhstore.db.api import get_session, get_engine
from pyhstore.models.user_hstore import UserHstore


def add_user(info):
    # add
    session = get_session()
    with session.begin(subtransactions=True):
        userHstore = UserHstore()
        userHstore.info = info
        session.add(userHstore)


def get_user_all():
    # get all
    session = get_session()
    with session.begin(subtransactions=True):
        return session.query(UserHstore).all()


def get_user_matrix():
    # get matrix
    session = get_session()
    with session.begin(subtransactions=True):
        return session.query(UserHstore.info.matrix()).all()


def get_user_keys():
    # get keys
    session = get_session()
    with session.begin(subtransactions=True):
        return session.query(UserHstore.info.keys()).all()


def get_user_values():
    # get values
    session = get_session()
    with session.begin(subtransactions=True):
        return session.query(UserHstore.info.vals()).all()


def get_user_by_has_all(in_list):
    # get by list in keys
    session = get_session()
    with session.begin(subtransactions=True):
        return session.query(UserHstore).filter(UserHstore.info.has_all(in_list)).all()


def get_user_by_has_any(in_list):
    # get by list while any in key
    session = get_session()
    with session.begin(subtransactions=True):
        return session.query(UserHstore).filter(UserHstore.info.has_any(in_list)).all()


def user_contains_key_value(key, value):
    # contains
    session = get_session()
    with session.begin(subtransactions=True):
        return session.query(UserHstore).filter(UserHstore.info.contains({key: value})).one()


def user_constains_key(key):
    # has_key
    session = get_session()
    with session.begin(subtransactions=True):
        user = session.query(UserHstore).filter(UserHstore.info.has_key(key)).first()
        if user:
            return True
        return False


def get_user_by_key_equal_value(key, value):
    # get by key/value
    session = get_session()
    with session.begin(subtransactions=True):
        return session.query(UserHstore).filter(UserHstore.info[key] == value).first()


def edit_user_by_key_value(key, value1, value2):
    # update key while key exist
    session = get_session()
    session.query(UserHstore).filter(UserHstore.info[key] == value1).update(
        {UserHstore.info: UserHstore.info + {key: value2, }, },
        synchronize_session="fetch")


def add_user_new_key_value_by_name(key, value, name):
    # # update key while key not exist
    session = get_session()
    with session.begin(subtransactions=True):
        session.query(UserHstore).filter(UserHstore.info['name'] == name).update(
            {UserHstore.info: UserHstore.info + {key: value, }, },
            synchronize_session="fetch")


def del_user_by_key(key1, key2):
    # del
    session = get_session()
    with session.begin(subtransactions=True):
        for user in session.query(UserHstore).filter(UserHstore.info.has_key(key1)):
            del user.info[key2]


def print_all_user_hstore():
    # print not service
    user_infos = get_user_all()
    r_list = []
    for user_info in user_infos:
        r_list.append([user_info.id, user_info.info])
    return r_list



