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

## Usage

This project supports saving quotations both on local file (JSON or CSV) and to Google spreadsheet, the latter requires you to have a Google service account.

To get started you must first create a JSON file that stores your Twitter credentials, see the `creds/twitter.json` for a template.
