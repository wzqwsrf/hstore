# 启动方式

首次clone

直接test
$ git clone git@github.com:wzqwsrf/hstore.git
$ cd hstore
$ tools/with_venv.sh python -m testtools.run tests.unit.test_user_service

pycharm test
修改绝对路径为相对路径.
注掉 CONF(['--config-file', 'tests/etc/unittest.ini'])
使用 CONF(['--config-file', '../etc/unittest.ini'])
$ python tools/install_venv.py
ctrl+shift+F10直接test


