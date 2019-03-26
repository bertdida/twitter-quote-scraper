import re
import json
import tweepy
import gspread
from oauth2client.service_account import ServiceAccountCredentials

with open('twitter_creds.json', 'r') as creds_file:
    twitter_creds = json.load(creds_file)

CONSUMER_KEY = twitter_creds.get('consumer_key')
CONSUMER_KEY_SECRET = twitter_creds.get('consumer_key_secret')
ACCESS_TOKEN = twitter_creds.get('access_token')
ACCESS_TOKEN_SECRET = twitter_creds.get('access_token_secret')

CODEWISDOM_ID = '396238794'
MIN_LIKE_COUNT = 1000

SERVICE_ACCOUNT_FILE = 'google_service_account.json'
SPREADSHEET_ID = '1U41EhnxXkWSJhmSqkPLpdbdcWJcx1MS6zWV3wQPeKL4'
INPUT_OPTION = 'USER_ENTERED'
SAVED_WISDOMS_RANGE = 'B2:B'
SAVED_ID_RANGE = 'D2'
SCOPES = ['https://spreadsheets.google.com/feeds']


WISDOM_AUTHOR_RE = re.compile(
    r'^[\"“](?P<wisdom>.*)[\"”]\s*?[\-–―]\s*(?P<author>.*)$')


def main():

    twitter_auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
    twitter_auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    twitter_api = tweepy.API(twitter_auth)

    google_creds = ServiceAccountCredentials.from_json_keyfile_name(
        SERVICE_ACCOUNT_FILE, SCOPES)
    google_client = gspread.authorize(google_creds)
    google_sheet = google_client.open_by_key(SPREADSHEET_ID)

    worksheet = google_sheet.sheet1
    worksheet_name = worksheet.title

    saved_wisdoms_range = '{}!{}'.format(worksheet_name, SAVED_WISDOMS_RANGE)
    saved_wisdoms = google_sheet.values_get(saved_wisdoms_range).get('values')
    saved_wisdoms = {w for [w] in saved_wisdoms} if saved_wisdoms else set()

    saved_id = worksheet.acell(SAVED_ID_RANGE).value or None

    new_wisdoms = set()
    request_body = []
    latest_tweet_id = None

    for status in tweepy.Cursor(twitter_api.user_timeline,
                                user_id=CODEWISDOM_ID,
                                since_id=saved_id,
                                tweet_mode='extended').items():

        json = status._json

        is_retweet = json.get('retweeted_status')
        is_reply = json.get('in_reply_to_status_id')
        is_unwanted = json.get('favorite_count') < MIN_LIKE_COUNT

        if any([is_retweet, is_reply, is_unwanted]):
            continue

        tweet_id = json.get('id_str')
        tweet_context = json.get('full_text')

        for hashtag_entity in json.get('entities').get('hashtags'):
            hashtag = '#{}'.format(hashtag_entity.get('text'))
            tweet_context = tweet_context.replace(hashtag, '')

        match = WISDOM_AUTHOR_RE.match(tweet_context)

        if match:
            url = 'https://twitter.com/CodeWisdom/status/{}'.format(tweet_id)
            wisdom = match.group('wisdom').strip()
            author = match.group('author').strip()

            if wisdom not in saved_wisdoms and wisdom not in new_wisdoms:
                if latest_tweet_id is None:
                    latest_tweet_id = tweet_id

                new_wisdoms.add(wisdom)
                request_body.insert(0, [author, wisdom, url])

    google_sheet.values_append(
        worksheet_name,
        params={'valueInputOption': INPUT_OPTION},
        body={'values': request_body})

    google_sheet.values_update(
        '{}!{}'.format(worksheet_name, SAVED_ID_RANGE),
        params={'valueInputOption': INPUT_OPTION},
        body={'values': [[latest_tweet_id]]})


if __name__ == '__main__':
    main()
