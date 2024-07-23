import tkinter as tk
from tkinter import Toplevel
from tkinter import ttk
from PIL import Image,ImageTk
cholates={
    '5 Star':'5 star.jpg',
    'Dairymilk':'dairymilk.jpg',
    'Dark cholate':'dark cholate.jpg',
    'kinderjoy':'kinderjoy.jpg',
    'kitkat':'kitkat.jpg',
    'Milkybar':'milkybar.jpg',
    'Snickers':'snickers.jpg'
    }
def show_cholate_image():
    selected_cholate=cholate_combobox.get()
    if selected_cholate:
        new_window=Toplevel(root)
        new_window.title(selected_cholate)
        img=Image.open(cholates[selected_cholate])
        img=ImageTk.PhotoImage(img)
        img_label=tk.Label(new_window,image=img)
        img_label.image=img
        img_label.pack()
root=tk.Tk()
root.title("cholate love")
root.geometry("800x600")
background_image=Image.open("cholates.jpg")
background_image=ImageTk.PhotoImage(background_image)
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)
frame=tk.Frame(root,bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')
cholate_combobox = ttk.Combobox(frame,values=list(cholates.keys()),state='readonly')
cholate_combobox.set("select a cholate")
cholate_combobox.pack(side=tk.LEFT, padx=10, pady=10)
show_button=tk.Button(frame, text="Show cholate",  command=show_cholate_image)
show_button.pack(side=tk.LEFT, padx=10, pady=10)
root.mainloop()
        
        

