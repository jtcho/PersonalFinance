from jt.util.conf_loader import read_conf


class FinanceService(object):

    def __init__(self):
        self.service_name = 'finances'
        self._conf = read_conf(self.service_name)

    @property
    def config(self):
        return self._conf


service = FinanceService()
