## Usage

```shell
python app.py --twitter-creds [command] [<arguments>]
```

##### `--twitter-creds`

Think of this argument as a login form for Twitter's API. Its value should be the path to JSON file that holds your Twitter app's credentials, see `creds/twitter.json` for the expected keys.


### Saving to a file

```shell
python app.py --twitter-creds local_file [<arguments>]
```

#### Arguments

##### `--twitter-handles`
An argument for `local_file` and `database` command. List of Twitter handles (may or may not start with @ character) to scrape.