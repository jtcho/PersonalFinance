import os

from oauth2client import client
from oauth2client import tools

from jt.finances.service import service as fin_service


def get_credentials(client_secret, scopes, application_name):
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    return fin_service.google_api_credentials
