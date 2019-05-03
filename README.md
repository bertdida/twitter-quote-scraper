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