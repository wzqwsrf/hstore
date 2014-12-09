# !/usr/bin/env python
# -*- coding: utf-8 -*-

from oslo.config import cfg
from testtools import TestCase
from fixture import DataSet, SQLAlchemyFixture
import fixtures

from pyhstore.db.db_connect import get_engine
from pyhstore.services.user_service import (add_user,
                                            get_user_by_key_equal_value,
                                            edit_user_by_key_value,
                                            add_user_new_key_value_by_name,
                                            del_user_by_key, user_constains_key)
from pyhstore.models.user_hstore import UserHstore

CONF = cfg.CONF


class UserData(DataSet):
    class user:
        id = 100
        info = dict(name='yazhou.liu',
                    company='lashou')


class DBConnectionFixture(fixtures.Fixture):
    def setUp(self):
        super(DBConnectionFixture, self).setUp()
        # CONF(['--config-file', 'tests/etc/unittest.ini'])
        CONF(['--config-file', '../etc/unittest.ini'])


class DBFixture(fixtures.Fixture):
    def setUp(self):
        super(DBFixture, self).setUp()
        self.dbfixture = SQLAlchemyFixture(
            engine=get_engine(),
            env=dict(UserData=UserHstore)
        )
        self.data = self.dbfixture.data(UserData)
        self.data.setup()
        self.addCleanup(self.data.teardown)


class TestUser(TestCase):
    def setUp(self):
        super(TestUser, self).setUp()
        self.useFixture(DBConnectionFixture())
        self.useFixture(DBFixture())

    def test_add_user(self):
        dic = {}
        dic['name'] = 'zhenqing.wang'
        dic['company'] = 'Qunar'
        add_user(dic)
        self.assertTrue('Qunar', get_user_by_key_equal_value('name', 'zhenqing.wang').info['company'])

    def test_edit_user_by_key_value(self):
        key = 'company'
        value1 = 'Qunar'
        value2 = 'Baidu'
        edit_user_by_key_value(key, value1, value2)
        self.assertTrue('Baidu', get_user_by_key_equal_value('name', 'zhenqing.wang').info['company'])

    def test_add_user_new_key_value_by_name(self):
        key = 'home'
        value = 'shanxi'
        name = 'zhenqing.wang'
        add_user_new_key_value_by_name(key, value, name)
        self.assertTrue(25, user_constains_key(key))

    def test_del_user_by_key(self):
        key1 = 'home'
        key2 = 'home'
        del_user_by_key(key1, key2)
        self.assertFalse(False, user_constains_key(key2))

    def test_user_constains_key(self):
        key = 'name'
        self.assertTrue(True, user_constains_key(key))