from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from cached_property import cached_property

from oauth2client.file import Storage

from jt.util.conf_loader import read_conf


class FinanceService(object):

    def __init__(self):
        self.service_name = 'finances'
        self._conf = read_conf(self.service_name)

        db_conf = read_conf('db')
        db_name = db_conf.db_name
        self.db_engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(db_conf.user,
                                                                               db_conf.password,
                                                                               db_conf.host,
                                                                               db_conf.port,
                                                                               db_name))
        self.session = sessionmaker()
        self.session.configure(bind=self.db_engine)

        self.google_api_credentials = Storage(self._conf.google_api_secret).get()

    @property
    def config(self):
        return self._conf

    @cached_property
    def dbsession(self):
        return self.session()


service = FinanceService()
dbsession = service.dbsession
