# 启动方式

首次clone

```sh

$ git clone ...
$ cd hstore
$ python tools/install_venv.py
$ tools/with_venv.sh python setup.py develop
s
```

前端调试服务器

```sh

$ tools/with_venv.sh itdb-www --config-file=etc/development/itdb.conf

```
