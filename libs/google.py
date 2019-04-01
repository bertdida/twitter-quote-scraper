import gspread
from oauth2client.service_account import ServiceAccountCredentials

INPUT_OPTION = 'USER_ENTERED'
SCOPES = ['https://spreadsheets.google.com/feeds']


class Sheet:

    def __init__(self, service_account_file: str, spreadsheet_id: str):

        creds = ServiceAccountCredentials.from_json_keyfile_name(
            service_account_file, SCOPES)
        client = gspread.authorize(creds)

        self.spreadsheet = client.open_by_key(spreadsheet_id)

    def get_worksheets(self):

        return self.spreadsheet.worksheets()

    def get_values(self, range_):

        # The API may return None, so when that happen set values to empty list
        values = self.spreadsheet.values_get(range_).get('values') or []

        for [value] in values:
            yield value

    def append(self, range_, request_body: list):

        self.spreadsheet.values_append(
            range_,
            params={'valueInputOption': INPUT_OPTION},
            body={'values': request_body})

    def update(self, range_, request_body: list):

        self.spreadsheet.values_update(
            range_,
            params={'valueInputOption': INPUT_OPTION},
            body={'values': request_body})
