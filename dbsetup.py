import sqlite3, json
from sqlite3 import Error


def create_connection(database):
    try:
        conn = sqlite3.connect(database, isolation_level=None, check_same_thread = False)
        conn.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))

        return conn
    except Error as e:
        print(e)


def create_table(c):
    sql = '''
        CREATE TABLE IF NOT EXISTS articles (
            id, integer PRIMARY KEY,
            name, varchar(225) NOT NULL,
            body, varchar(225) NOT NULL
        );
    '''
    c.execute(sql)


def insert_db(c, name, body):
    sql = ''' INSERT INTO articles(name, body) VALUE (?, ?) '''
    C.execute(sql, (name, body))


def select_all_items(c, name):
    c.execute("SELECT * FROM articles WHERE name like ?", ('%'+name+'%',))
    rows = c.fetchall()
    return rows


def main():
    database = './sqlite.db'

    conn = create_connection(database)

    create_table(conn)

    print("Connection established!")


if __name__ == '__main__':
    main()
