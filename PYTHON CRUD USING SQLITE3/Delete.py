import sqlite3
from tkinter import messagebox
def Delete(id):
    try:
        conn=sqlite3.connect('mydatabase.db')
        c=conn.cursor()
        c.execute("DELETE FROM mytable WHERE id =?",(id,))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success','Data updated successfully')
    except sqlite3.Error as e:
        messagebox.showinfo('Error',e)
    finally:
        conn.close()
