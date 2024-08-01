import sqlite3
from tkinter import messagebox

def Create():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()  # Add cursor creation
    cursor.execute("CREATE TABLE IF NOT EXISTS mytable (myname TEXT, id TEXT PRIMARY KEY)")
    conn.close()

def InsertData(name, id):
    Create()
    try:
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO mytable (myname, id) VALUES (?, ?)", (name, id))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success', 'Data inserted successfully')
    except sqlite3.Error as e:
        messagebox.showerror('Error', str(e))  # Corrected messagebox method and error message
    finally:
        if conn:
            conn.close()

# Example usage
# InsertData("John Doe", "12345678")

