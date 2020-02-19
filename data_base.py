import sqlite3 as sql

class DataBase(object):

    def base_list(self):

        con = sql.connect('base.db')
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS 'base'('list1' BINARY 'list2' BINARY)")
        con.commit()
        cur.close()