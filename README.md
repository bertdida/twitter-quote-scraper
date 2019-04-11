# TwitterQuoteScraper

So I think creating an API regarding programming quotes is fun, by fun I mean lots of learnings. That's why I created this project to provide the most fundamental data of my ideal API, quotes.

TwitterQuoteScraper enables you to collect tweets from any Twitter accounts who share motivational phrases taken from a book, movie or someone.

Example spreadsheet can be found [here](https://docs.google.com/spreadsheets/d/1U41EhnxXkWSJhmSqkPLpdbdcWJcx1MS6zWV3wQPeKL4/edit?usp=sharing).

## Notes

- Tweets that are a retweet, reply, has URL or media (image or video) and any emojis are ignored.
- This project is highly dependent on regular expression. A Tweet should match this pattern to be included: `^[\"\']{0,1}(?P<phrase>[A-Z].*[\.!?])[\"\']{0,1}\s*?[-~]\s*(?P<author>.*)$`.

## Prerequisites

- Python 3.6
- [Pipenv](https://github.com/pypa/pipenv)
- Google service account
- Twitter API Keys and Tokens

## Installation

1. Download the [zip file](https://github.com/bertdida/TwitterQuoteScraper/archive/master.zip) or use Git to clone the repository.
2. Inside the directory open a terminal and run `pipenv install`.

## Setup

### Google spreadsheet

1. Login on Google and create a spreadsheet.
2. Create a header by inserting Author, Phrase, and URL on the first row.
3. Click the number beside the first row (this highlights the row) and click View > Freeze.
4. Rename the first sheet to the desired Twitter handle you want to scrape (may or may not start with @ character).

### Codebase

1. Inside the `creds` folder, open `google.example.json` and `twitter.example.json` then place your Google service account and Twitter keys respectively.
2. Rename `google.example.json` and `twitter.example.json` to remove `.example`.
3. Go back to Google spreadsheet and give a Can Edit access to the `client_email` you'll find inside the `google.json`.

## Usage

From the terminal run the following commands:

1. `pipenv shell`
2. `python app.py`

## Tested Twitter handles

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
- [emoji](https://github.com/carpedm20/emoji/) - used to check and ignore tweets that have an emoji
- [unidecode](https://github.com/avian2/unidecode) - used to convert tweets' Unicode special characters to ASCII

## License

Distributed under the MIT license. See LICENSE for more information.

## Author

Herbert Verdida / [@bertdida](https://twitter.com/bertdida)
