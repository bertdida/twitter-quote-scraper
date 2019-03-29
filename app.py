import json
import gspread
from libs import helpers, GoogleSheet, TwitterQuoteScraper
from oauth2client.service_account import ServiceAccountCredentials

TWITTER_CREDS_FILE = 'creds/twitter.json'
SERVICE_ACCOUNT_FILE = 'creds/google.json'

SPREADSHEET_ID = '1U41EhnxXkWSJhmSqkPLpdbdcWJcx1MS6zWV3wQPeKL4'
SAVED_PHRASES_RANGE = 'B2:B'
SAVED_ID_RANGE = 'D1'


with open(TWITTER_CREDS_FILE, 'r') as twitter_creds_file:
    twitter_creds = json.load(twitter_creds_file)

twitter_scraper = TwitterQuoteScraper(twitter_creds)
google_sheet = GoogleSheet(SERVICE_ACCOUNT_FILE, SPREADSHEET_ID)

for worksheet in google_sheet.get_worksheets():
    worksheet_name = worksheet.title

    saved_phrases_range = '{}!{}'.format(worksheet_name, SAVED_PHRASES_RANGE)
    saved_id_range = '{}!{}'.format(worksheet_name, SAVED_ID_RANGE)

    saved_phrases_alphanum = set()
    for phrase in google_sheet.get_values(saved_phrases_range):
        saved_phrases_alphanum.add(helpers.to_lowercased_alphanum(phrase))

    [saved_id] = google_sheet.get_values(saved_id_range) or [None]

    new_quotes = twitter_scraper.get_quotes(worksheet_name, saved_id)
    new_quotes_unique = []

    for quote in new_quotes:
        phrase_alphanum = helpers.to_lowercased_alphanum(quote.phrase)

        if phrase_alphanum not in saved_phrases_alphanum:
            new_quotes_unique.insert(0, quote)
            saved_phrases_alphanum.add(phrase_alphanum)

    if new_quotes_unique:
        *_, latest_quote = new_quotes_unique
        *_, latest_quote_id = latest_quote.url.split('/')

        google_sheet.update(saved_id_range, [[latest_quote_id]])
        google_sheet.append(worksheet_name, new_quotes_unique)
