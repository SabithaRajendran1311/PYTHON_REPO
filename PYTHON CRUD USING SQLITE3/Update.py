from tkinter import messagebox
import sqlite3

def Update(name, id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute("UPDATE mytable SET myname=? WHERE id=?", (name, id))
        conn.commit()
        messagebox.showinfo('Success', 'Data updated successfully')
    except sqlite3.Error as e:
        messagebox.showinfo('Error', str(e))
    finally:
        conn.close()

