import tkinter as tk
from tkinter import messagebox
class FormApp:
    def __init__(self,root):
        self.root=root
        self.root.title("User Information Form")
        self.create_widgets()
    def create_widgets(self):
      tk.Label(self.root,text="First Name").grid(row=0,column=0,padx=10,pady=5)
      tk.Label(self.root,text="Last Name").grid(row=1,column=0,padx=10,pady=5)
      tk.Label(self.root,text="Age").grid(row=2,column=0,padx=10,pady=5)
      tk.Label(self.root,text="Gender").grid(row=3,column=0,padx=10,pady=5)
      tk.Label(self.root,text="Email").grid(row=4,column=0,padx=10,pady=5)
      self.first_name_entry=tk.Entry(self.root)
      self.last_name_entry=tk.Entry(self.root)
      self.age_entry=tk.Entry(self.root)
      self.gender_var=tk.StringVar()
      self.email_entry=tk.Entry(self.root)
      self.first_name_entry.grid(row=0,column=1,padx=10,pady=5)
      self.last_name_entry.grid(row=1,column=1,padx=10,pady=5)
      self.age_entry.grid(row=2,column=1,padx=10,pady=5)
      self.gender_frame=tk.Frame=tk.Frame(self.root)
      self.gender_frame.grid(row=3,column=1,padx=10,pady=5)
      tk.Radiobutton(self.gender_frame,text="Male",variable=self.gender_var,value="Male").pack(side=tk.LEFT)
      tk.Radiobutton(self.gender_frame,text="Female",variable=self.gender_var,value="Female").pack(side=tk.LEFT)
      tk.Radiobutton(self.gender_frame,text="Other",variable=self.gender_var,value="Other").pack(side=tk.LEFT)
      self.email_entry.grid(row=4,column=1,padx=10,pady=5)
      self.submit_button=tk.Button(self.root,text="Submit",command=self.submit_form)
      self.submit_button.grid(row=5,columnspan=2,pady=10)
    def submit_form(self):
      first_name=self.first_name_entry.get()
      last_name=self.last_name_entry.get()
      age=self.age_entry.get()
      gender=self.gender_var.get()
      email=self.email_entry.get()
      messagebox.showinfo("form submitted",f"name:{first_name}{last_name}\nage:{age}\nGender{gender}\Email:{email}")
root=tk.Tk()
app=FormApp(root)
root.mainloop()
