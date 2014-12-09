# !/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


def get_engine():
    engine = create_engine('postgres://postgres:postgres@localhost/hstore', echo=True)
    return engine


def get_session():
    engine = get_engine()
    session_all = sessionmaker(bind=engine)
    session = session_all(autocommit=True)
    return session


def get_session_not_commit():
    engine = get_engine()
    session_all = sessionmaker(bind=engine)
    session = session_all()
    return session
