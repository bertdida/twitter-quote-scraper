import os
import csv
import json


class LocalFile:

    supported_formats = ('json', 'csv')

    def __init__(self, file_type, output_folder):

        self.file_type = file_type

        self.output_folder = output_folder
        os.makedirs(os.path.dirname(self.output_folder), exist_ok=True)

    def get_file_path(self, twitter_handle):

        return os.path.join(
            self.output_folder,
            '{}.{}'.format(twitter_handle, self.file_type))

    def read(self, file_path):

        if not os.path.exists(file_path):
            return []

        with open(file_path, 'r') as infile:
            if self.file_type == 'json':
                quotes = json.loads(infile.read())
            else:
                reader = csv.DictReader(infile)
                quotes = [dict(r) for r in reader]

            return quotes

    def write(self, file_path, quotes):

        with open(file_path, 'w') as outfile:
            if self.file_type == 'json':
                json.dump(quotes, fp=outfile, indent=4)

            else:
                writer = csv.DictWriter(outfile,
                                        fieldnames=quotes[0].keys())

                writer.writeheader()
                writer.writerows(quotes)
