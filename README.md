## Usage

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
Database and each Twitter handle's table will be generated if doesn't exist.

```shell
# Single account
python app.py --twitter-creds creds/twitter.json database --twitter-handles @prog_quotes --database-configs creds/database.json

# Multiple accounts
python app.py --twitter-creds creds/twitter.json database --twitter-handles @prog_quotes @CodeWisdom --database-configs creds/database.json

# Ignore warnings
python -W ignore app.py --twitter-creds creds/twitter.json database --twitter-handles @prog_quotes --database-configs c reds/database.json
```

### Saving to Google spreadsheet

Before you run the command, follow the steps below to set up a Google spreadsheet.
1. Log in to Google and make a copy of the spreadsheet's template.
2. Share the spreadsheet with the `client_email` you can find inside your Google service account's JSON file.

```shell
# Make sure to change the --spreadsheet-id's value
python app.py --twitter-creds creds/twitter.json google_sheet --service-account creds/google.json --spreadsheet-id 1S8xsN8D6nD2KM5-oSZOIFnuw3zvP4_WRZLHMMfbsbPk

# Sort the second column alphabetically
python app.py --twitter-creds creds/twitter.json google_sheet --service-account creds/google.json --spreadsheet-id 1S8xsN8D6nD2KM5-oSZOIFnuw3zvP4_WRZLHMMfbsbPk --sort '{"order": "asc", "column": 1}'
```

## References

### Commands

**local_file**  Generate and save quotations to a file.

usage: `python app.py --twitter-creds local_file --twitter-handles [--output-folder] [--file-type]`

<br>

**database** Save quotations to MySQL database.

usage: `python app.py --twitter-creds database --twitter-handles --database-configs`

<br>

**google_sheet** Save quotations to Google spreadsheet.

usage: `python app.py --twitter-creds google_sheet --service-account --spreadsheet-id [--sort]`

### Arguments

**--twitter-creds** Path to JSON file that contains your Twitter app's credentials, see `creds/twitter.json` for the expected keys. This argument should take place before every command, think of this as a login form to access Twitter's API.

<br>

**--twitter-handles** List of Twitter handles to scrape (may or may not start with @ character).

commands: `local_file`, `database`

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

**--service-account** Path to your Google service account's JSON file. If you have not yet created, [this](https://www.fillup.io/post/read-and-write-google-sheets-from-php/) blog outlines how to get one.

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