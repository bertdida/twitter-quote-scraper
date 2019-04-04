from typing import List
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

    def get_values(self, range_: str):

        # Set values to empty list if the API returns None.
        values = self.spreadsheet.values_get(range_).get('values') or []

        for [value] in values:
            yield value

    def append(self, range_: str, request_body: List[list]):

        self.spreadsheet.values_append(
            range_,
            params={'valueInputOption': INPUT_OPTION},
            body={'values': request_body})

    def update(self, range_: str, request_body: List[list]):

        self.spreadsheet.values_update(
            range_,
            params={'valueInputOption': INPUT_OPTION},
            body={'values': request_body})

    def sort(self, sheet_name: str, column: int = 0, order: str = 'ASCENDING'):
        '''Sort the values of the given sheet name.

        Args:
            sheet_name: The name of the sheet to be sorted.
            column: The column of the sheet where the sort should be applied to.
            order: The order of the data on sort. Supported values are the following:
                        - ASCENDING
                        - DESCENDING
                        - SORT_ORDER_UNSPECIFIED
        '''

        sheet_id = self.spreadsheet.worksheet(sheet_name).id

        request_body = [{
            'sortRange': {
                'range': {
                    'sheetId': sheet_id,
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

        self.spreadsheet.batch_update(
            body={'requests': request_body})
