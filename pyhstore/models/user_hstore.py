# !/usr/bin/env python
# -*- coding: utf-8 -*-
# wangzhenqing (wangzhenqing1008@163.com)
# Date: 2014年12月08日17:04:19

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import HSTORE
from sqlalchemy.ext.mutable import MutableDict

Base = declarative_base()


class UserHstore(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    info = Column(MutableDict.as_mutable(HSTORE))

    def __repr__(self):
        return "<Player('%s','%s')>" % (self.id, self.info)