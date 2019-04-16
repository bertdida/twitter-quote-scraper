<p align="center"><img src="/logo/logotype-horizontal.png"></p>

# TwitterQuoteScraper

**Important:** This README is not yet updated.

So I think creating an API regarding programming quotes is fun, by fun I mean lots of learnings. That's why I created this project to provide the most fundamental data of my ideal API, quotes.

TwitterQuoteScraper collects and parses tweets from any Twitter accounts who share motivational sayings or paraphrases.

Example spreadsheet can be found [here](https://docs.google.com/spreadsheets/d/1U41EhnxXkWSJhmSqkPLpdbdcWJcx1MS6zWV3wQPeKL4/edit?usp=sharing).

## Notes

- Tweets that are a retweet, reply, has URL or media (image or video) and any emoji are disregarded.
- This project highly depends on a regular expression. A Tweet should match this pattern to be considered as a quote: `^[\"\']{0,1}(?P<phrase>[A-Z].*[\.!?])[\"\']{0,1}\s*?[-~]\s*(?P<author>.*)$`.

## Prerequisites

- Python 3.6
- [Pipenv](https://github.com/pypa/pipenv)
- Google service account
- Twitter API Keys and Tokens

## Installation

1. Download and extract the [zip file](https://github.com/bertdida/TwitterQuoteScraper/archive/master.zip) or use Git to clone the repository.
2. Inside the directory open a terminal and run `pipenv install`.

## Setup

### Google spreadsheet

1. Login on your Google account and create a spreadsheet.
2. On the top menu click View > Freeze > 1 row.
3. Insert Author, Phrase, and URL on each column of the first row.
4. Rename the first sheet to the desired Twitter handle you want to scrape (may or may not start with @ character).

### Codebase

1. Within the `creds` folder, update `google.json` and `twitter.json` with your Google service account and Twitter keys respectively.
2. Open `app.py` and edit `SPREADSHEET_ID` with your Google spreadsheet's id.
3. Go back to the spreadsheet and give a Can Edit access to the `client_email` you'll find inside `creds/google.json`.

## Usage

From the terminal run the following commands:

1. `pipenv shell`
2. `python app.py`

## Tested Twitter handles

| Twitter handle                                          | Date of testing | Total tweets | Total quotes |
| ------------------------------------------------------- | --------------- | ------------ | ------------ |
| [@GreatestQuotes](https://twitter.com/GreatestQuotes)   | 04/11/2019      | 34543        | 3165         |
| [@CodeWisdom](https://twitter.com/CodeWisdom)           | 04/11/2019      | 3218         | 1952         |
| [@KH_Quote](https://twitter.com/KH_Quote)               | 04/11/2019      | 63383        | 2844         |
| [@AQuotesPage](https://twitter.com/AQuotesPage)         | 04/11/2019      | 96011        | 2541         |
| [@SportsMotto](https://twitter.com/SportsMotto)         | 04/11/2019      | 291          | 235          |
| [@Sports_Greats](https://twitter.com/Sports_Greats)     | 04/11/2019      | 86628        | 1137         |
| [@CoachMotto](https://twitter.com/CoachMotto)           | 04/11/2019      | 330          | 280          |
| [@QuoteOfHumanity](https://twitter.com/QuoteOfHumanity) | 04/11/2019      | 541          | 0            |
| [@prog_quotes](https://twitter.com/prog_quotes)         | 04/11/2019      | 21           | 20           |
| [@RunningQuotes](https://twitter.com/RunningQuotes)     | 04/11/2019      | 5496         | 947          |
| [@motivational](https://twitter.com/motivational)       | 04/11/2019      | 21205        | 2015         |
| [@DeepLifeQuotes](https://twitter.com/DeepLifeQuotes)   | 04/11/2019      | 9641         | 1065         |
| [@bukowski_quote](https://twitter.com/bukowski_quote)   | 04/11/2019      | 90122        | 1228         |
| [@Quote_Club](https://twitter.com/Quote_Club)           | 04/11/2019      | 2056         | 608          |
| [@inventess](https://twitter.com/inventess)             | 04/11/2019      | 4034         | 2914         |

## Dependencies

- [tweepy](https://github.com/tweepy/tweepy)
- [gspread](https://github.com/burnash/gspread)
- [oauth2client](https://github.com/googleapis/oauth2client)
- [emoji](https://github.com/carpedm20/emoji/) - used to check and ignore tweets that have an emoji
- [unidecode](https://github.com/avian2/unidecode) - used to convert tweets' Unicode special characters to ASCII

## Contribute

If you have any problem, idea or suggestion, feel free to create issues and pull requests.

## License

Distributed under the MIT license. See LICENSE for more information.

## Author

Herbert Verdida / [@bertdida](https://twitter.com/bertdida)

Logo by [@Tobaloidee](https://github.com/Tobaloidee)
