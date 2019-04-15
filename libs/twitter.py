import re
import html
import emoji
import tweepy
import unidecode
import collections
from typing import List

QUOTE_PATTERN = \
    re.compile(r'^[\"\']{0,1}(?P<phrase>[A-Z].*[\.!?])[\"\']{0,1}'
               r'\s*?[-~]\s*'
               r'(?P<author>.*)$')

SPECIAL_CHARS_PATTERN = re.compile(r'[^a-zA-Z0-9]')

Quote = collections.namedtuple('Quote', 'author phrase url')


class QuoteScraper:

    def __init__(self, creds: dict):

        auth = tweepy.OAuthHandler(
            creds.get('consumer_key'),
            creds.get('consumer_key_secret'))

        auth.set_access_token(
            creds.get('access_token'),
            creds.get('access_token_secret'))

        self.api = tweepy.API(auth)

    def get_quotes(self, twitter_handle: str, tweet_since_id=None):

        twitter_handle = twitter_handle.lstrip('@')
        base_url = 'https://twitter.com/{}'.format(twitter_handle)

        for tweet in tweepy.Cursor(self.api.user_timeline,
                                   screen_name=twitter_handle,
                                   since_id=tweet_since_id,
                                   tweet_mode='extended').items():

            if not self.is_allowed(tweet):
                continue

            tweet_text = self.get_normalized_tweet_text(tweet)
            match = QUOTE_PATTERN.match(tweet_text)

            if match:
                url = '{}/status/{}'.format(base_url, tweet.id_str)
                phrase = html.unescape(match.group('phrase').strip())
                author = html.unescape(match.group('author').strip())

                yield Quote(author, phrase, url)

    @staticmethod
    def is_allowed(tweet):

        # To avoid Attribute error, use the JSON version of the tweet object.
        is_retweet = tweet._json.get('retweeted_status')

        is_reply = tweet.in_reply_to_status_id
        has_url = tweet.entities.get('urls')
        has_media = tweet.entities.get('media')
        has_emoji = bool(emoji.get_emoji_regexp().search(tweet.full_text))

        return not any([is_retweet,
                        is_reply,
                        has_url,
                        has_media,
                        has_emoji])

    def get_normalized_tweet_text(self, tweet):

        strip_hashtags = self.strip_hashtags(tweet.entities.get('hashtags'))

        text = strip_hashtags(tweet.full_text)
        text = self.special_chars_to_ascii(text)
        text = text.replace('--', '-')

        return text

    @staticmethod
    def strip_hashtags(hashtag_entities: List[dict]):

        hashtags = ['#{}'.format(e.get('text')) for e in hashtag_entities]

        def _strip_hashtags(tweet_context):

            for hashtag in hashtags:
                tweet_context = tweet_context.replace(hashtag, '')

            return tweet_context

        return _strip_hashtags

    @staticmethod
    def special_chars_to_ascii(tweet_context):

        new_tweet_context = []

        for char in tweet_context:

            if SPECIAL_CHARS_PATTERN.match(char):
                char = unidecode.unidecode(char)

            new_tweet_context.append(char)

        return ''.join(new_tweet_context)
