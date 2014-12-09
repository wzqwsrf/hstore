# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2014年12月09日16:25:23
# Auther: wangzhenqing(wangzhenqing1008@163.com)

from oslo.config import cfg
from oslo.db import options
from testtools import TestCase
from fixture import DataSet, SQLAlchemyFixture
import fixtures

from pyhstore.db.api import get_engine, get_session
from pyhstore.models.user_hstore import UserHstore
from pyhstore.services.user_service import (
    add_user,
    get_user_by_key_equal_value,
    edit_user_by_key_value,
    add_user_new_key_value_by_name,
    del_user_by_key, user_constains_key,
    print_all_user_hstore,
    get_user_keys,
    get_user_values,
    get_user_by_has_all,
    get_user_by_has_any,
    get_user_matrix,
    user_contains_key_value
)

CONF = cfg.CONF
CONF.register_opts(options.database_opts, 'database')


class UserData(DataSet):
    class user1:
        info = dict(name='yazhou.liu',
                    company='lashou')

    class user2:
        info = dict(name='zhenqing.wang',
                    company='qunar')

    class user3:
        info = dict(name='lucy',
                    age='25')


class DBConnectionFixture(fixtures.Fixture):
    def setUp(self):
        super(DBConnectionFixture, self).setUp()
        CONF(['--config-file', 'tests/etc/unittest.ini'])
        # CONF(['--config-file', '../etc/unittest.ini'])


class DBFixture(fixtures.Fixture):
    def setUp(self):
        super(DBFixture, self).setUp()
        self.session = get_session()
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
        self.dbfixture = self.useFixture(DBFixture())
        self.session = self.dbfixture.session

    def tearDown(self):
        super(TestUser, self).tearDown()
        self.session.execute('delete from users')

    def test_add_user(self):
        name = 'test_name'
        company = 'test_company'
        dic = dict(name=name, company=company)
        add_user(dic)
        print 'test_add_user'
        print print_all_user_hstore()
        self.assertEqual(company, get_user_by_key_equal_value('name', name).info['company'])

    def test_edit_user_by_key_value(self):
        key = 'company'
        value1 = 'qunar'
        value2 = 'Baidu'
        edit_user_by_key_value(key, value1, value2)
        print 'test_edit_user_by_key_value'
        print print_all_user_hstore()
        print get_user_by_key_equal_value('name', 'zhenqing.wang').info['company']
        self.assertEqual('Baidu', get_user_by_key_equal_value('name', 'zhenqing.wang').info['company'])

    def test_add_user_new_key_value_by_name(self):
        key = 'home'
        value = 'beijing'
        name = 'zhenqing.wang'
        add_user_new_key_value_by_name(key, value, name)
        print 'test_add_user_new_key_value_by_name'
        print print_all_user_hstore()
        self.assertEqual(True, user_constains_key(key))

    def test_del_user_by_key(self):
        key1 = 'home'
        key2 = 'home'
        del_user_by_key(key1, key2)
        print 'test_del_user_by_key'
        print print_all_user_hstore()
        self.assertEqual(False, user_constains_key(key2))

    def test_user_constains_key(self):
        key = 'name'
        print 'test_user_constains_key'
        print print_all_user_hstore()
        self.assertEqual(True, user_constains_key(key))

    def test_get_user_keys(self):
        user_infos = get_user_keys()
        print 'test_get_user_keys'
        print user_infos
        self.assertEqual(3, len(user_infos))

    def test_get_user_values(self):
        user_infos = get_user_values()
        print 'test_get_user_values'
        print user_infos
        self.assertEqual(3, len(user_infos))

    def test_get_user_by_has_all(self):
        in_list = ['name', 'company']
        user_infos = get_user_by_has_all(in_list)
        print 'test_get_user_by_has_all'
        print user_infos
        self.assertEqual(2, len(user_infos))

    def test_get_user_by_has_any(self):
        in_list = ['name']
        user_infos = get_user_by_has_any(in_list)
        print 'test_get_user_by_has_any'
        print user_infos
        self.assertEqual(3, len(user_infos))
        in_list = ['age']
        user_infos = get_user_by_has_any(in_list)
        print 'test_get_user_by_has_any'
        print user_infos
        self.assertEqual(1, len(user_infos))

    def test_get_user_matrix(self):
        user_infos = get_user_matrix()
        print 'test_get_user_matrix'
        print user_infos
        print type(user_infos[0])
        self.assertEqual(3, len(user_infos))
        self.assertEqual(1, len(user_infos[0]))

    def test_user_contains_key_value(self):
        key = 'name'
        value = 'zhenqing.wang'
        user_info = user_contains_key_value(key, value)
        print 'test_user_contains_key_value'
        print user_info
        self.assertEqual(value, user_info.info[key])
