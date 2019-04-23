<p align="center"><img src="logo/logotype-horizontal.png"></p>

# TwitterQuoteScraper

_One day I was thinking about creating a web application that displays quotations randomly. There are lots of this on [CodePen](https://codepen.io/search/pens?q=random%20quote%20generator&page=1&order=popularity&depth=everything), but I want to experience on how to develop both of its frontend and backend functionalities. I need the data first, and I assume Twitter can help me with this!_

TwitterQuoteScraper is a command line tool with a purpose to help in scraping quotations from the desired Twitter accounts.

## Behaviors

- Tweets that are a retweet, reply, has URL or media (image or video) and any emoji are disregarded.
- This project highly depends on a regular expression. A tweet should match the pattern to be considered as a quotation: `^[\"\']{0,1}(?P<phrase>[A-Z].*[\.!?])[\"\']{0,1}\s*?[-~]\s*(?P<author>.*)$`.
- When using a Google spreadsheet, values will be sorted by phrase column alphabetically.

## Prerequisites

- Python 3.6
- [Pipenv](https://github.com/pypa/pipenv)
- [Twitter API Keys and Tokens](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html)
- [Google service account](https://developers.google.com/sheets/api/guides/authorizing) (only if you want to use Google spreadsheet)

## Installation

1. Download and extract the [zip file](https://github.com/bertdida/TwitterQuoteScraper/archive/master.zip) or use Git to clone this repository.
2. Inside the directory open a terminal and run `pipenv install`.

## Usage

Currently, TwitterQuoteScraper supports saving quotations to a local file or into Google spreadsheet. But either of these ways you must first create a JSON file that holds your Twitter app's credentials (see `creds/twitter.json`), this file's path is required every time you run a command to scrape quotations.

To maintain consistency, this section will use `creds/twitter.json` and `creds/google.json` as the values for `--twitter-creds` and `--service-account` respectively. Don't forget to change these to the actual path of your JSON files.

To learn more about a command's usage and syntax, like which options are available and the command's structure you may run the following:

- `python app.py -h`
- `python app.py --twitter-creds creds/twitter.json local_file -h`
- `python app.py --twitter-creds creds/twitter.json google_sheet -h`

### Saving to a local file

Usage example:

```shell
# Single account
python app.py --twitter-creds creds/twitter.json local_file --twitter-handles @prog_quotes

# Multiple accounts
python app.py --twitter-creds creds/twitter.json local_file --twitter-handles @prog_quotes @CodeWisdom

# Specify the folder where the files will be generated
python app.py --twitter-creds creds/twitter.json local_file --twitter-handles @prog_quotes --output-folder quotes

# Override the default file type
python app.py --twitter-creds creds/twitter.json local_file --twitter-handles @prog_quotes --file-type json
```

### Saving to Google spreadsheet

Before you run the command, set up a Google spreadsheet first.

1. Log in to Google and make a copy of the [template spreadsheet](https://docs.google.com/spreadsheets/d/1S8xsN8D6nD2KM5-oSZOIFnuw3zvP4_WRZLHMMfbsbPk/edit?usp=sharing).
2. Share the spreadsheet with the `client_email` you can find inside your Google service account's JSON file.

Usage example:

```shell
python app.py --twitter-creds creds/twitter.json google_sheet --service-account creds/google.json --spreadsheet-id 1S8xsN8D6nD2KM5-oSZOIFnuw3zvP4_WRZLHMMfbsbPk
```

Here's an example of a [spreadsheet](https://docs.google.com/spreadsheets/d/1U41EhnxXkWSJhmSqkPLpdbdcWJcx1MS6zWV3wQPeKL4/edit?usp=sharing) that was set up to be updated daily via CRON job.

## Dependencies

- [tweepy](https://github.com/tweepy/tweepy)
- [gspread](https://github.com/burnash/gspread)
- [oauth2client](https://github.com/googleapis/oauth2client)
- [emoji](https://github.com/carpedm20/emoji/) - used to check and ignore tweets that have an emoji
- [unidecode](https://github.com/avian2/unidecode) - used to convert tweets' unicode special characters to ASCII

## Contribute

If you have any problem, idea or suggestion, feel free to create issues and pull requests.

## License

Distributed under the MIT license. See LICENSE for more information.

## Author

Herbert Verdida / [@bertdida](https://twitter.com/bertdida)

## Thanks

My gratitude to [@Tobaloidee](https://github.com/Tobaloidee) for making this project's awesome logo.
