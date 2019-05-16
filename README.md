<h1 align="center"><img alt="logo" src="logo/logotype-horizontal.png"></h1>

[![Maintainability](https://api.codeclimate.com/v1/badges/91583eca09bd1e2f163b/maintainability)](https://codeclimate.com/github/bertdida/TwitterQuoteScraper/maintainability)
[![codebeat badge](https://codebeat.co/badges/24297975-d0d0-4185-8b41-ad84e53f241b)](https://codebeat.co/projects/github-com-bertdida-twitterquotescraper-master)
[![License: MIT](https://img.shields.io/github/license/bertdida/TwitterQuoteScraper.svg)](https://github.com/bertdida/TwitterQuoteScraper/blob/master/LICENSE)
[![Known Vulnerabilities](https://snyk.io/test/github/bertdida/TwitterQuoteScraper/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/bertdida/TwitterQuoteScraper?targetFile=requirements.txt)

_I want to build a random quote generator, something like [forismatic.com](https://forismatic.com/en/). Thinking where to get some data, I remember a [Twitter account](https://twitter.com/CodeWisdom) I followed that posts curated computer programming quotes. And the rest... was pythoning._

TwitterQuoteScraper is a command line tool with a purpose to help in scraping quotations from the desired Twitter accounts.

**Note:** For the tweet to be considered as a quotation the following conditions must be satisfied:
- tweet must not be a retweet or a reply
- must not contain URL, media (image or video) or any emoji
- must match the regular expression: `^[\"\']{0,1}(?P<phrase>[A-Z].*[\.!?])[\"\']{0,1}\s*?[-~]\s*(?P<author>.*)$`

## Prerequisites

- Python 3.6
- [Pipenv](https://github.com/pypa/pipenv)
- [Twitter API Keys and Tokens](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html)
- Google service account (required only if the `google_sheet` command is used) - [this](https://www.fillup.io/post/read-and-write-google-sheets-from-php/) blog has simplified outlines on getting one

## Installation

1. Download and extract the [zip file](https://github.com/bertdida/TwitterQuoteScraper/archive/master.zip) or use Git to clone this repository.
2. Inside the directory open a terminal and run:

   ```shell
   pipenv install
   ```

## Usage

**Important:** Make sure to activate the virtual environment first, doing this will put the virtual environment-specific python and pip executables into pipenv shell’s `PATH`; this can be done using:

```shell
pipenv shell
```

To learn more about the command's usage and syntax, like which options are available and the command's structure run the following:

- `python app.py -h`
- `python app.py --twitter-creds creds/twitter.json local_file -h`
- `python app.py --twitter-creds creds/twitter.json database -h`
- `python app.py --twitter-creds creds/twitter.json google_sheet -h`

### Saving to a local file

```shell
# Single account
python app.py --twitter-creds creds/twitter.json local_file --twitter-handles @prog_quotes

# Multiple accounts
python app.py --twitter-creds creds/twitter.json local_file --twitter-handles @prog_quotes @CodeWisdom

# Specify the folder where the files will be generated
python app.py --twitter-creds creds/twitter.json local_file --twitter-handles @prog_quotes --output-folder quotes/

# Override the default file type
python app.py --twitter-creds creds/twitter.json local_file --twitter-handles @prog_quotes --file-type json
```

### Saving to MySQL database

The Database and each Twitter handle's table will be created if it doesn't exist.

```shell
# Single account
python app.py --twitter-creds creds/twitter.json database --twitter-handles @prog_quotes --database-configs creds/database.json

# Multiple accounts
python app.py --twitter-creds creds/twitter.json database --twitter-handles @prog_quotes @CodeWisdom --database-configs creds/database.json

# Ignore warnings
python -W ignore app.py --twitter-creds creds/twitter.json database --twitter-handles @prog_quotes --database-configs creds/database.json
```

### Saving to Google spreadsheet

Before you run the command, you must set up a Google spreadsheet for the service account to programmatically insert and edit values.

1. Log in to Google and create a spreadsheet.
2. Share the spreadsheet with the `client_email` you'll find inside the Google service account's JSON file.

```shell
# Make sure to change --spreadsheet-id's value

python app.py --twitter-creds creds/twitter.json google_sheet --service-account creds/google.json --spreadsheet-id 1S8xsN8D6nD2KM5-oSZOIFnuw3zvP4_WRZLHMMfbsbPk --twitter-handles @prog_quotes

# Alphabetically sort the second column
python app.py --twitter-creds creds/twitter.json google_sheet --service-account creds/google.json --spreadsheet-id 1S8xsN8D6nD2KM5-oSZOIFnuw3zvP4_WRZLHMMfbsbPk --twitter-handles @prog_quotes --sort '{"order": "asc", "column": 1}'
```

The command of [this spreadsheet](https://docs.google.com/spreadsheets/d/1U41EhnxXkWSJhmSqkPLpdbdcWJcx1MS6zWV3wQPeKL4/edit?usp=sharing) is set up to run every midnight UTC time via CRON job.

## References

### Commands

**local_file** Generate and save quotations to a file.

usage: `python app.py --twitter-creds local_file --twitter-handles [--output-folder] [--file-type]`

<br>

**database** Save quotations to MySQL database.

usage: `python app.py --twitter-creds database --twitter-handles --database-configs`

<br>

**google_sheet** Save quotations to Google spreadsheet.

usage: `python app.py --twitter-creds google_sheet --service-account --spreadsheet-id --twitter-handles [--sort]`

### Arguments

**--twitter-creds** Path to JSON file that contains your Twitter app's credentials, see `creds/twitter.json` for the expected keys. This argument should take place before every command, think of this as a login form to access Twitter's API.

<br>

**--twitter-handles** List of Twitter handles to scrape (may or may not start with @ character).

commands: `local_file`, `database`, `google_sheet`

<br>

**--output-folder** The folder where the files will be generated; by default, its value is set to the current working directory.

commands: `local_file`

<br>

**--file-type** The file's format to be generated, choose either `CSV` (default) or `JSON`.

commands: `local_file`

<br>

**--database-configs** Path to database configurations' JSON file, see `creds/database.json` for keys.

commands: `database`

<br>

**--service-account** Path to your Google service account's JSON file.

commands: `google_sheet`

<br>

**--spreadsheet-id** The spreadsheet's ID.

commands: `google_sheet`

<br>

**--sort** A JSON-formatted string that specifies how to sort the spreadsheet's values; by default, its value is set to:

```javascript
{
    "order": null,  // expects the following values: null, "asc" or "desc"
    "column": 0     // column's number where the sort should be applied to
}
```

commands: `google_sheet`

## Dependencies

- [tweepy](https://github.com/tweepy/tweepy)
- [gspread](https://github.com/burnash/gspread)
- [oauth2client](https://github.com/googleapis/oauth2client)
- [emoji](https://github.com/carpedm20/emoji/)
- [unidecode](https://github.com/avian2/unidecode)
- [pymysql](https://github.com/PyMySQL/PyMySQL)

## License

Distributed under the MIT license. See [LICENSE](https://github.com/bertdida/TwitterQuoteScraper/blob/master/LICENSE) for more information.

## Author

Herbert Verdida / [@bertdida](https://twitter.com/bertdida)

## Credits

Thanks to [@Tobaloidee](https://github.com/Tobaloidee) for making this project's logo.
