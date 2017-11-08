#! /usr/bin/env python

from sqlalchemy import create_engine
from jt.util.conf_loader import read_conf

db_conf = read_conf('db')
db_name = db_conf.db_name
engine = create_engine('mysql+mysqldb://{}:{}@{}:{}'.format(db_conf.user,
                                                            db_conf.password,
                                                            db_conf.host,
                                                            db_conf.port))
engine.execute('DROP DATABASE {}'.format(db_name))
engine.execute('CREATE DATABASE IF NOT EXISTS {}'.format(db_name))
engine.execute('USE {}'.format(db_name))
print('Finished!')
