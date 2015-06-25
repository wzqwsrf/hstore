## 关于hstore
------
1. postgresql中hstore数据类型的增删改查。
2. python项目。
3. virtualenv隔离虚拟环境。


## 运行
------
####直接运行方式

1. `git clone git@github.com:wzqwsrf/hstore.git`
2. `cd hstore**`
3. 这一步是为了安装需要的第三方依赖包，`python tools/install_venv.py`
4. 运行测试用例，`tools/with_venv.sh python -m testtools.run tests.unit.test_user_service`

####使用pycharm
1. 修改绝对路径为相对路径。
2. 注掉 CONF(['--config-file', 'tests/etc/unittest.ini'])，使用 CONF(['--config-file', '../etc/unittest.ini']) 
3. python tools/install_venv.py 
4. ctrl+shift+F10直接test


## 关于postgresql中的hstore类型
------
参考：<http://blog.csdn.net/u013027996/article/details/40115563>
