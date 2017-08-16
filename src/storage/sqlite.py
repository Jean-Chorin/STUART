import sqlite3 as lite
import sys


database_name = "test.db"


def sqlite_version():
    """ Just give the current version of sqlite as a string """

    con = lite.connect(database_name)

    with con:
        
        cur = con.cursor()    
        cur.execute('SELECT SQLITE_VERSION()')
        
        data = cur.fetchone()
        
        return("SQLite version: {}".format(data))


if __name__ == '__main__':
    print(sqlite_version())
