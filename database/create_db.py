import sqlite3
import os

PATH_DB = 'sklad_db.sqlite3'


class Connector:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()


class DbBuilder(Connector):

    def create_table(self, name_tb):
        path_to_script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sql_scripts')
        path_to_script = os.path.join(path_to_script_dir, f'{name_tb}.sql')
        with open(path_to_script) as f:
            self.cur.executescript(f.read())
        self.conn.close()

    def drop_table(self, name_tb):
        self.cur.execute(f'DROP TABLE IF EXISTS {name_tb}')


if __name__ == '__main__':
    # Создание даблиц в БД
    builder = DbBuilder(PATH_DB)
    #builder.create_table('categories')
    #builder.create_table('units')
    #builder.create_table('goods')
    #builder.create_table('positions')
    #builder.create_table('employees')
    #builder.create_table('vendors')

    # Создание таблиц в тестовой БД
    #builder = DbBuilder('test_mapper_db.sqlite')
    #builder.create_table('vendors')
    #builder.create_table('units')
    #builder.create_table('categories')
    #builder.create_table('goods')

