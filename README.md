## Usage
```shell
python app.py --twitter-creds [command] [<arguments>]
```

#### `--twitter-creds`
Think of this as a log in form for Twitter's API. It is the path to JSON file that contains the Twitter app's credentials, see `creds/twitter.json` for the expected keys.

### Commands

#### `local_file`
Generates and saves quotations to a file.

```shell
python app.py --twitter-creds local_file [<arguments>]
```

### Arguments
#### `--twitter-handles`
List of Twitter handles to scrape. The values may or may not start with the @ character.

#### `--output-folder`
The folder where the files will be generated, the current working directory is its default value.

#### `--file-type`
The generated file's type, either `CSV` or `JSON` format.