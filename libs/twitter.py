import re
import html
import emoji
import unidecode
import tweepy
import collections
from typing import List
from .helpers import compose

QUOTE_PATTERN = \
    re.compile(r'^[\"\']{0,1}(?P<phrase>[A-Z].*[\.!?])[\"\']{0,1}'
               r'\s*?[-~]\s*'
               r'(?P<author>.*)$')

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

    def get_quotes(self, tweeter_handle: str, tweet_since_id: str):

        tweeter_handle = tweeter_handle.lstrip('@')
        base_url = 'https://twitter.com/{}'.format(tweeter_handle)

        for tweet in tweepy.Cursor(self.api.user_timeline,
                                   screen_name=tweeter_handle,
                                   since_id=tweet_since_id,
                                   tweet_mode='extended').items():

            tweet_id = tweet.id_str
            tweet_context = tweet.full_text
            tweet_entities = tweet.entities

            # To avoid Attribute error, use the json version of the tweet object.
            is_retweet = tweet._json.get('retweeted_status')

            is_reply = tweet.in_reply_to_status_id
            has_url = tweet_entities.get('urls')
            has_media = tweet_entities.get('media')
            has_emoji = self.has_emoji(tweet_context)

            if any([is_retweet,
                    is_reply,
                    has_url,
                    has_media,
                    has_emoji]):
                continue

            hashtag_entities = tweet_entities.get('hashtags')
            _strip_hashtags = self.strip_hashtags(hashtag_entities)

            normalize_tweet = compose(_strip_hashtags,
                                      self.convert_special_chars_to_ascii,
                                      lambda s: s.replace('--', '-'))  # em dash

            tweet_context = normalize_tweet(tweet_context)
            match = QUOTE_PATTERN.match(tweet_context)

            if match:
                url = '{}/status/{}'.format(base_url, tweet_id)
                phrase = self.strip_and_unescape(match.group('phrase'))
                author = self.strip_and_unescape(match.group('author'))

                yield Quote(author, phrase, url)

    @staticmethod
    def has_emoji(tweet_context):

        return emoji.get_emoji_regexp().search(tweet_context) is not None

    @staticmethod
    def strip_hashtags(hashtag_entities: List[dict]):

        hashtags = ['#{}'.format(e.get('text')) for e in hashtag_entities]

        def _strip_hashtags(tweet_context):

            for hashtag in hashtags:
                tweet_context = tweet_context.replace(hashtag, '')

            return tweet_context

        return _strip_hashtags

    @staticmethod
    def convert_special_chars_to_ascii(tweet_context):

        new_tweet_context = []

        for char in tweet_context:
            ascii_ = unidecode.unidecode(char)
            new_tweet_context.append(char if ascii_.isalpha() else ascii_)

        return ''.join(new_tweet_context)

    @staticmethod
    def strip_and_unescape(tweet_context):

        function = compose(lambda s: s.strip(),
                           lambda s: html.unescape(s))

        return function(tweet_context)
