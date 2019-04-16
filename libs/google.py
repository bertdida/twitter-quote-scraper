import gspread
from oauth2client.service_account import ServiceAccountCredentials

INPUT_OPTION = 'USER_ENTERED'
SCOPES = ['https://spreadsheets.google.com/feeds']


class Sheet:

    def __init__(self, service_account_file, spreadsheet_id):

        creds = ServiceAccountCredentials\
            .from_json_keyfile_name(service_account_file, SCOPES)

        client = gspread.authorize(creds)

        self.spreadsheet = client.open_by_key(spreadsheet_id)

    @property
    def worksheets(self):

        return self.spreadsheet.worksheets()

    def get_values(self, range_):

        values = self.spreadsheet.values_get(range_).get('values')
        values = [] if values is None else values

        for [value] in values:
            yield value

    def append(self, range_, request_body):

        self.spreadsheet.values_append(
            range_,
            params={'valueInputOption': INPUT_OPTION},
            body={'values': request_body})

    def update(self, range_, request_body):

        self.spreadsheet.values_update(
            range_,
            params={'valueInputOption': INPUT_OPTION},
            body={'values': request_body})

    def sort(self, worksheet_name, column=0, order='ASCENDING'):

        worksheet_id = self.spreadsheet.worksheet(worksheet_name).id

        request_body = [{
            'sortRange': {
                'range': {
                    'sheetId': worksheet_id,
                    'startRowIndex': 1  # exclude headers
                },
                'sortSpecs': [
                    {
                        'dimensionIndex': column,
                        'sortOrder': order
                    }
                ]
            }
        }]

        self.spreadsheet.batch_update(body={'requests': request_body})
