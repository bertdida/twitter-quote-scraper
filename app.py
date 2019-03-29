import json
import helpers
import gspread
from twitter import QuoteScraper
from oauth2client.service_account import ServiceAccountCredentials

TWITTER_CREDS_FILE = 'creds/twitter.json'
SERVICE_ACCOUNT_FILE = 'creds/google.json'

SPREADSHEET_ID = '1U41EhnxXkWSJhmSqkPLpdbdcWJcx1MS6zWV3wQPeKL4'
INPUT_OPTION = 'USER_ENTERED'
SAVED_QUOTES_RANGE = 'B2:B'
SAVED_ID_RANGE = 'D1'
SCOPES = ['https://spreadsheets.google.com/feeds']

CODEWISDOM_ID = '396238794'

google_creds = ServiceAccountCredentials.from_json_keyfile_name(
    SERVICE_ACCOUNT_FILE, SCOPES)
google_client = gspread.authorize(google_creds)
google_sheet = google_client.open_by_key(SPREADSHEET_ID)

worksheet = google_sheet.sheet1
worksheet_name = worksheet.title

saved_quotes_range = '{}!{}'.format(worksheet_name, SAVED_QUOTES_RANGE)
saved_quotes = google_sheet.values_get(saved_quotes_range).get('values') or []
saved_quotes_alphanum = \
    {helpers.to_lowercased_alphanum(q) for [q] in saved_quotes}

saved_id = worksheet.acell(SAVED_ID_RANGE).value or None

with open(TWITTER_CREDS_FILE, 'r') as twitter_creds_file:
    twitter_creds = json.load(twitter_creds_file)

scraper = QuoteScraper(twitter_creds)
new_quotes = scraper.get_quotes(CODEWISDOM_ID, saved_id)

new_quotes_unique = []
for author, quote, url in new_quotes:
    quote_alphanum = helpers.to_lowercased_alphanum(quote)

    if quote_alphanum not in saved_quotes_alphanum:
        saved_quotes_alphanum.add(quote_alphanum)
        new_quotes_unique.insert(0, [author, quote, url])

*_, latest_quote = new_quotes_unique
*_, latest_quote_url = latest_quote
*_, latest_quote_id = latest_quote_url.split('/')

google_sheet.values_append(
    worksheet_name,
    params={'valueInputOption': INPUT_OPTION},
    body={'values': new_quotes_unique})

google_sheet.values_update(
    '{}!{}'.format(worksheet_name, SAVED_ID_RANGE),
    params={'valueInputOption': INPUT_OPTION},
    body={'values': [[latest_quote_id]]})
