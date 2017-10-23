from __future__ import print_function
import httplib2

from apiclient import discovery

from jt.finances.google_api_service import get_credentials
from jt.finances.service import service as fin_service

class SpreadsheetFetchClient(object):

    def __init__(self):
        conf = fin_service.config
        self.client_secret = conf.client_secret
        self.google_scopes = conf.google_scopes
        self.application_name = conf.application_name
        self.discovery_url = conf.discovery_url

    def fetch_spreadsheet(self, sheet_range):
        conf = fin_service.config
        credentials = get_credentials(self.client_secret, self.google_scopes,
                                      self.application_name)
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('sheets', 'v4', http=http,
                                  discoveryServiceUrl=self.discovery_url)
        result = service.spreadsheets()\
                        .values()\
                        .get(spreadsheetId=conf.spreadsheet_id,
                             range=sheet_range)\
                        .execute()
        return result.get('values', [])

fetch_client = SpreadsheetFetchClient()

