## Usage

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

### Saving to MySQL database

```shell
# Database and tables will be generated if doesn't exist
python app.py --twitter-creds creds/twitter.json database --twitter-handles @prog_quotes --database-configs creds/database.json

# Do not display warnings
python -W ignore app.py --twitter-creds creds/twitter.json database --twitter-handles @prog_quotes --database-configs c reds/database.json
```

## Commands

**local_file**  Generate and save quotations to a file.

usage: `python app.py --twitter-creds local_file --twitter-handles [--output-folder] [--file-type]`

<br>

**database** Save quotations to MySQL database.

usage: `python app.py --twitter-creds database --twitter-handles --database-configs`

<br>

**google_sheet** Save quotations to Google spreadsheet.

usage: `python app.py --twitter-creds google_sheet --service-account --spreadsheet-id [--sort]`

## Arguments

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