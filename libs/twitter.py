import re
import html
import emoji
import tweepy
import unidecode
import collections

QUOTE_PATTERN = \
    re.compile(r'^[\"\']{0,1}(?P<phrase>[A-Z].*[\.!?])[\"\']{0,1}'
               r'\s*?[-~]\s*'
               r'(?P<author>.*)$')

Quote = collections.namedtuple('Quote', 'author phrase url')


class QuoteScraper:

    def __init__(self, creds: dict):

        auth = tweepy.OAuthHandler(
            creds['consumer_key'],
            creds['consumer_key_secret'])

        auth.set_access_token(
            creds['access_token'],
            creds['access_token_secret'])

        self.api = tweepy.API(auth)

    def get_quotes(self, handle, since_id=None):

        base_url = 'https://twitter.com/{}'.format(handle.lstrip('@'))

        for status in tweepy.Cursor(self.api.user_timeline,
                                    id=handle,
                                    since_id=since_id,
                                    tweet_mode='extended').items():

            if not self.is_allowed(status):
                continue

            tweet = self.get_normalized_tweet(status)
            match = QUOTE_PATTERN.match(tweet)

            if match is None:
                continue

            url = '{}/status/{}'.format(base_url, status.id_str)
            phrase = html.unescape(match.group('phrase').strip())
            author = html.unescape(match.group('author').strip())

            yield Quote(author, phrase, url)

    @staticmethod
    def is_allowed(status):

        is_retweet = hasattr(status, 'retweeted_status')
        is_reply = status.in_reply_to_status_id
        has_url = status.entities.get('urls')
        has_media = status.entities.get('media')
        has_emoji = emoji.get_emoji_regexp().search(status.full_text)

        return not any([is_retweet,
                        is_reply,
                        has_url,
                        has_media,
                        has_emoji])

    @classmethod
    def get_normalized_tweet(cls, status):

        tweet = status.full_text
        tweet = cls.strip_hashtags(tweet, status.entities.get('hashtags'))
        tweet = cls.non_alphanum_chars_to_ascii(tweet)
        tweet = tweet.strip()

        return tweet.replace('--', '-')

    @staticmethod
    def strip_hashtags(tweet, hashtag_entities):

        for hashtag_entity in hashtag_entities:
            hashtag = '#{}'.format(hashtag_entity.get('text'))
            tweet = tweet.replace(hashtag, '')

        return tweet

    @staticmethod
    def non_alphanum_chars_to_ascii(tweet):
        """Convert characters that do not evaluate to alphanumeric into ASCII.
        """

        retval = []

        for char in tweet:
            char_ascii = unidecode.unidecode(char)
            retval.append(char if char_ascii.isalpha() else char_ascii)

        return ''.join(retval)
