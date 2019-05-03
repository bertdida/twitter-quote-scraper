## Usage
```shell
python app.py --twitter-creds [command] [<arguments>]
```

#### `--twitter-creds`
Think of this argument as a login form for Twitter's API. Its value should be the path to JSON file that holds your Twitter app's credentials, see `creds/twitter.json` for the expected keys.

---

#### `local_file`
Command to generate and save quotations to a file.

#### `database`
Command to save quotations to MySQL database.

#### `google_sheet`
Command to save quotations to Google spreadsheet.

---

### `--twitter-handles`
An argument for `local_file` and `database` command. List of Twitter handles (may or may not start with @ character) to scrape.