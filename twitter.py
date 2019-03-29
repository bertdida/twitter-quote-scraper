import re
import html
import emoji
import tweepy
import unidecode
from helpers import compose


class API():

    def __new__(cls, creds: dict):

        auth = tweepy.OAuthHandler(
            creds.get('consumer_key'),
            creds.get('consumer_key_secret'))

        auth.set_access_token(
            creds.get('access_token'),
            creds.get('access_token_secret'))

        return tweepy.API(auth)


class QuoteScraper:

    QUOTE_AUTHOR_RE = re.compile(r'^"(?P<quote>.*)"\s*?-\s*?(?P<author>.*)$')

    def __init__(self, twitter_creds: dict):

        self.api = TwitterAPI(twitter_creds)

    def get_quotes(self, user_id: str, since_id: str):

        for tweet in tweepy.Cursor(self.api.user_timeline,
                                   user_id=user_id,
                                   since_id=since_id,
                                   tweet_mode='extended').items():

            data = tweet._json

            tweet_id = data.get('id_str')
            tweet_context = data.get('full_text')
            tweet_entities = data.get('entities')

            normalize_tweet = compose(self.strip_emojis,
                                      self.strip_hashtags(tweet_entities),
                                      self.to_ascii,
                                      lambda s: s.replace('--', '-'))

            tweet_context = normalize_tweet(tweet_context)

            is_retweet = data.get('retweeted_status')
            is_reply = data.get('in_reply_to_status_id')
            has_url = tweet_entities.get('urls')
            has_media = tweet_entities.get('media')
            match = QUOTE_AUTHOR_RE.match(tweet_context)

            if any([is_retweet,
                    is_reply,
                    has_url,
                    has_media,
                    match is None]):
                continue

            url = 'https://twitter.com/CodeWisdom/status/{}'.format(tweet_id)
            quote = self.strip_and_unescape(match.group('quote'))
            author = self.strip_and_unescape(match.group('author'))

            yield [author, quote, url]

    @staticmethod
    def strip_emojis(tweet_context):

        return emoji.get_emoji_regexp().sub('', tweet_context)

    @staticmethod
    def strip_hashtags(tweet_entities: dict):

        hashtag_entities = tweet_entities.get('hashtags')
        hashtags = ['#{}'.format(e.get('text')) for e in hashtag_entities]

        def _strip_hashtags(tweet_context):

            for hashtag in hashtags:
                tweet_context = tweet_context.replace(hashtag, '')

            return tweet_context

        return _strip_hashtags

    @staticmethod
    def to_ascii(tweet_context):

        return unidecode.unidecode(tweet_context)

    @staticmethod
    def strip_and_unescape(tweet_context):

        function = compose(lambda s: s.strip(),
                           lambda s: html.unescape(s))

        return function(tweet_context)
