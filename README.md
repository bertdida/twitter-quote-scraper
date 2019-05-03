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

**--twitter-creds** The path to JSON file that holds your Twitter app's credentials, see `creds/twitter.json` for the expected keys.

<br>

**--twitter-handles** List of Twitter handles (may or may not start with @ character) to scrape.

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

**--service-account** Path to your Google service account's JSON file. Follow the [Acquiring and using an API key](https://developers.google.com/sheets/api/guides/authorizing) tutorial if you don't have yet.

commands: `google_sheet`

<br>

**--spreadsheet-id** The spreadsheet's ID.

commands: `google_sheet`

<br>

**--sort** A JSON-like string that specifies how to sort the spreadsheet's values; the default value is set to (without comments):

```javascript
{
    // The sort order, supported values are:
    // - null: default, do not sort
    // - "asc": sort by ascending
    // - "desc": sort by descending
    "order": null,

    // The column's number where the sort
    // should be applied to.
    "column": 0
}
```

commands: `google_sheet`