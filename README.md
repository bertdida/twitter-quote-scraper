<p align="center"><img src="logo/logotype-horizontal.png"></p>

# TwitterQuoteScraper

TwitterQuoteScraper is a command line tool with a purpose to help in scraping quotations from the desired Twitter accounts.

## Prerequisites

- Python 3.6
- [Pipenv](https://github.com/pypa/pipenv)
- Twitter API Keys and Tokens
- Google service account (optional)

## Installation

1. Download and extract the [zip file](https://github.com/bertdida/TwitterQuoteScraper/archive/master.zip) or use Git to clone this repository.
2. Inside the directory open a terminal and run `pipenv install`.

## Tested Twitter accounts

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
