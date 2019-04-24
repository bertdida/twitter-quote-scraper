import re
import os
import csv
import json
import argparse
from libs import google, twitter, localfile


def main():
    parser = argparse.ArgumentParser(
        description='Scrapes quotations from Twitter')

    parser.add_argument(
        '--twitter-creds',
        help='Path to JSON file that contains your Twitter app\'s '
             'consumer_key, consumer_key_secret, access_token and '
             'access_token_secret',
        required=True,
        type=argparse.FileType('r'))

    subparsers = parser.add_subparsers(title='command', dest='subparser')

    parser_google_sheet = subparsers.add_parser(
        'google_sheet',
        help='Saves quotations to Google spreadsheet')

    parser_local_file = subparsers.add_parser(
        'local_file',
        help='Generates and saves quotations to a file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser_google_sheet.add_argument(
        '--service-account',
        help='Path to Google service account\'s JSON file',
        required=True,
        type=argparse.FileType('r'))

    parser_google_sheet.add_argument(
        '--spreadsheet-id',
        help='The spreadsheet\'s ID',
        required=True,
        type=str)

    parser_local_file.add_argument(
        '--twitter-handles',
        help='List of Twitter handles to scrape',
        required=True,
        nargs='+',
        type=str)

    parser_local_file.add_argument(
        '--output-folder',
        help='The folder where the files will be generated',
        type=str,
        default=os.getcwd())

    parser_local_file.add_argument(
        '--file-type',
        help='The generated file\'s type',
        type=str,
        default='csv',
        choices=localfile.LocalFile.supported_file_types)

    parser_google_sheet.set_defaults(func=use_google_sheet)
    parser_local_file.set_defaults(func=use_local_file)

    args = parser.parse_args()

    if args.subparser is None:
        parser.print_help()
        exit(1)

    args.func(args)


def to_lowercase_alphanum(text):
    """Remove non-alphanumeric characters and convert text to lowercase.
    """

    return re.sub(r'[^a-z0-9]', '', text.lower())


def use_google_sheet(args):

    google_sheet = google.Sheet(args.service_account.name, args.spreadsheet_id)
    scraper = twitter.QuoteScraper(json.load(args.twitter_creds))

    for worksheet in google_sheet.worksheets:
        worksheet_name = worksheet.title

        saved_phrases_range = '{}!B2:B'.format(worksheet_name)
        saved_id_range = '{}!D1'.format(worksheet_name)

        saved_phrases = google_sheet.get_values(saved_phrases_range)
        saved_phrases_alphanum = {
            to_lowercase_alphanum(p) for p in saved_phrases}

        saved_id = (list(google_sheet.get_values(saved_id_range)) + [None])[0]

        quotes_unique = []
        for quote in scraper.get_quotes(worksheet_name, saved_id):
            phrase_alphanum = to_lowercase_alphanum(quote.phrase)

            if phrase_alphanum not in saved_phrases_alphanum:
                quotes_unique.insert(0, quote)
                saved_phrases_alphanum.add(phrase_alphanum)

        if quotes_unique:
            *_, latest_id = quotes_unique[-1].url.split('/')

            google_sheet.update(saved_id_range, [[latest_id]])
            google_sheet.append(worksheet_name, quotes_unique)
            google_sheet.sort(order='ASCENDING',
                              worksheet_name=worksheet_name,
                              column=1)


def use_local_file(args):

    local_file = localfile.LocalFile(args.file_type, args.output_folder)
    scraper = twitter.QuoteScraper(json.load(args.twitter_creds))

    for handle in args.twitter_handles:
        file_path = local_file.get_filepath(handle.lstrip('@'))

        saved_quotes = local_file.read(file_path)

        saved_phrases = [q['phrase'] for q in saved_quotes]
        saved_phrases_alphanum = {
            to_lowercase_alphanum(p) for p in saved_phrases}

        saved_id = None
        if saved_quotes:
            *_, saved_id = saved_quotes[0]['url'].split('/')

        quotes_unique = []
        for quote in scraper.get_quotes(handle, saved_id):
            phrase_alphanum = to_lowercase_alphanum(quote.phrase)

            if phrase_alphanum not in saved_phrases_alphanum:
                quote_dict = dict(quote._asdict())  # namedtuple to dict

                quotes_unique.append(quote_dict)
                saved_phrases_alphanum.add(phrase_alphanum)

        for quote in reversed(quotes_unique):
            saved_quotes.insert(0, quote)

        local_file.write(file_path, saved_quotes)


if __name__ == '__main__':
    main()
