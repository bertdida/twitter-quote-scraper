import re
import json
from libs import helpers, google, twitter

TWITTER_CREDS_FILE = 'creds/twitter.json'
SERVICE_ACCOUNT_FILE = 'creds/google.json'

SPREADSHEET_ID = '1U41EhnxXkWSJhmSqkPLpdbdcWJcx1MS6zWV3wQPeKL4'
SAVED_PHRASES_RANGE = 'B2:B'
SAVED_ID_RANGE = 'D1'

with open(TWITTER_CREDS_FILE, 'r') as creds_file:
    twitter_creds = json.load(creds_file)

google_sheet = google.Sheet(SERVICE_ACCOUNT_FILE, SPREADSHEET_ID)
twitter_scraper = twitter.QuoteScraper(twitter_creds)

for worksheet in google_sheet.get_worksheets():
    worksheet_name = worksheet.title

    saved_phrases_range = '{}!{}'.format(worksheet_name, SAVED_PHRASES_RANGE)
    saved_id_range = '{}!{}'.format(worksheet_name, SAVED_ID_RANGE)

    # Remove non-alphanumeric characters to reduce the possibility
    # of duplicate quotes.
    saved_phrases_alphanum = \
        {helpers.to_lowercased_alphanum(p)
         for p in google_sheet.get_values(saved_phrases_range)}

    [saved_id] = list(google_sheet.get_values(saved_id_range)) or [None]

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
        google_sheet.sort(
            order='ASCENDING', sheet_name=worksheet_name, column=1)
