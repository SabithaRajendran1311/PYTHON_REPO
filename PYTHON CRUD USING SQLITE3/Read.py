import sqlite3
def Read():
    conn=sqlite3.connect('mydatabase.db')
    cursor=conn.cursor()
    cursor.execute('SELECT*FROM mytable')
    all_rows=cursor.fetchall()
    conn.close()
    return all_rows

