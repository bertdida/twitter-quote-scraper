import pymysql
import pymysql.cursors


class MySQL:

    def __init__(self, configs: dict):

        self.connection = pymysql.connect(
            host=configs['host'],
            user=configs['user'],
            password=configs['password'],
            charset='utf8mb4',
            autocommit=True,
            cursorclass=pymysql.cursors.DictCursor)

        self.database_name = configs['database']

    def __enter__(self):

        with self.connection.cursor() as cursor:
            cursor.execute('CREATE DATABASE IF NOT EXISTS {} '
                           'CHARACTER SET utf8mb4 '
                           'COLLATE utf8mb4_unicode_ci'
                           .format(self.database_name))

        self.connection.select_db(self.database_name)
        return self

    def __exit__(self, *args):

        self.connection.close()

    def create_table(self, table_name):

        with self.connection.cursor() as cursor:
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS `{}` ('
                '`id` int(11) NOT NULL auto_increment,'
                '`author` varchar(255) NOT NULL,'
                '`phrase` varchar(255) NOT NULL,'
                '`url` varchar(255) NOT NULL,'
                'PRIMARY KEY(`id`)'
                ')'.format(table_name))

    def fetch_quotes(self, table_name):

        with self.connection.cursor() as cursor:
            cursor.execute('SELECT `author`, `phrase`, `url` FROM `{}` '
                           'ORDER BY `id` DESC'.format(table_name))

            result = cursor.fetchall()

        return result

    def save_quotes(self, table_name, quotes: list):

        with self.connection.cursor() as cursor:
            cursor.executemany(
                'INSERT INTO `{}` (`author`, `phrase`, `url`) '
                'VALUES (%s, %s, %s)'.format(table_name),
                quotes)
