import os
import csv
import json


class LocalFile:

    supported_file_types = ('json', 'csv')

    def __init__(self, file_type, output_folder):

        if not self.is_supported(file_type):
            raise ValueError('Not supported file type: {}'.format(file_type))

        self.file = JSON() if file_type == 'json' else CSV()
        self.file_type = file_type
        self.output_folder = '{}/'.format(output_folder.rstrip('/'))

        os.makedirs(os.path.dirname(self.output_folder), exist_ok=True)

    @classmethod
    def is_supported(cls, file_type):

        return file_type in cls.supported_file_types

    def get_filepath(self, file_name):

        return os.path.join(
            self.output_folder, '{}.{}'.format(file_name, self.file_type))

    def read(self, file_path) -> list:

        if not os.path.exists(file_path):
            return []

        return self.file.read(file_path)

    def write(self, file_path, quotes):

        if not quotes:
            return

        self.file.write(file_path, quotes)


class JSON:

    @staticmethod
    def read(file_path) -> list:

        with open(file_path, 'r') as infile:
            return json.loads(infile.read())

    @staticmethod
    def write(file_path, quotes):

        with open(file_path, 'w', encoding='utf-8') as outfile:
            json.dump(quotes, fp=outfile, indent=4)


class CSV:

    @staticmethod
    def read(file_path) -> list:

        with open(file_path, 'r') as infile:
            return [dict(q) for q in csv.DictReader(infile)]

    @staticmethod
    def write(file_path, quotes):

        with open(file_path, 'w', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=quotes[0].keys())

            writer.writeheader()
            writer.writerows(quotes)
