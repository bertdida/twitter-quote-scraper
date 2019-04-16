import os
import csv
import json


class LocalFile:

    supported_file_types = ('json', 'csv')

    def __init__(self, file_type, output_folder):

        if not self.is_supported(file_type):
            raise ValueError('Not supported file type: {}'.format(file_type))

        self.file_type = file_type
        self.output_folder = output_folder

        os.makedirs(os.path.dirname(self.output_folder), exist_ok=True)

    @classmethod
    def is_supported(cls, file_type):

        return file_type in cls.supported_file_types

    def get_filepath(self, file_name):

        return os.path.join(
            self.output_folder, '{}.{}'.format(file_name, self.file_type))

    def read(self, file_path):

        if not os.path.exists(file_path):
            return []

        with open(file_path, 'r') as infile:
            if self.file_type == 'json':
                quotes = json.loads(infile.read())
            else:
                quotes = [dict(q) for q in csv.DictReader(infile)]

            return quotes

    def write(self, file_path, quotes):

        if not quotes:
            return

        with open(file_path, 'w') as outfile:
            if self.file_type == 'json':
                json.dump(quotes, fp=outfile, indent=4)
            else:
                writer = csv.DictWriter(outfile, fieldnames=quotes[0].keys())

                writer.writeheader()
                writer.writerows(quotes)
