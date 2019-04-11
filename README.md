# TwitterQuoteScraper

Example spreadsheet can be found [here](https://docs.google.com/spreadsheets/d/1U41EhnxXkWSJhmSqkPLpdbdcWJcx1MS6zWV3wQPeKL4/edit?usp=sharing).

## Prerequisites

- [Python 3.6](https://www.python.org/downloads/release/python-360/)
- [Pipenv](https://github.com/pypa/pipenv)
- [Google service account](https://developers.google.com/android/management/service-account)
- [Twitter API Keys and Tokens](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html)

## Usage

1. Clone the repo by running `git clone https://github.com/bertdida/TwitterQuoteScraper.git`.
2. Update `creds/google.example.json` and `creds/twitter.example.json` with your Google service account and Twitter keys respectively.
3. Rename `creds/google.example.json` and `creds/twitter.example.json` to remove `.example`.
4. Create a Google spreadsheet and share with the `client_email` you can find inside `creds/google.json`.
5. Rename the first sheet to your desired Twitter handle.
6. Run `pipenv install`, `pipenv shell` then `app.py`.

## Tested handles

- [@GreatestQuotes](https://twitter.com/GreatestQuotes)
- [@CodeWisdom](https://twitter.com/CodeWisdom)
- [@KH_Quote](https://twitter.com/KH_Quote)
- [@AQuotesPage](https://twitter.com/AQuotesPage)
- [@SportsMotto](https://twitter.com/SportsMotto)
- [@Sports_Greats](https://twitter.com/Sports_Greats)
- [@CoachMotto](https://twitter.com/CoachMotto)
- [@RunningQuotes](https://twitter.com/RunningQuotes)
- [@QuoteOfHumanity](https://twitter.com/QuoteOfHumanity)
- [@motivational](https://twitter.com/motivational)
- [@DeepLifeQuotes](https://twitter.com/DeepLifeQuotes)
- [@bukowski_quote](https://twitter.com/bukowski_quote)
- [@Quote_Club](https://twitter.com/Quote_Club)
- [@inventess](https://twitter.com/inventess)
- [@prog_quotes](https://twitter.com/prog_quotes)

## Dependencies

- [tweepy](https://github.com/tweepy/tweepy)
- [gspread](https://github.com/burnash/gspread)
- [oauth2client](https://github.com/googleapis/oauth2client)
- [emoji](https://github.com/carpedm20/emoji/) - used to check and ignore tweets having emoji
- [unidecode](https://github.com/avian2/unidecode) - used to convert tweets' Unicode special characters to ASCII

## License

Distributed under the MIT license. See LICENSE for more information.

## Author

Herbert Verdida / [@bertdida](https://twitter.com/bertdida)
