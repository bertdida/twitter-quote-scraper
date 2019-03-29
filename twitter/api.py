import tweepy


class API():

    def __new__(cls, creds: dict):
        auth = tweepy.OAuthHandler(
            creds.get('consumer_key'),
            creds.get('consumer_key_secret'))

        auth.set_access_token(
            creds.get('access_token'),
            creds.get('access_token_secret'))

        return tweepy.API(auth)
