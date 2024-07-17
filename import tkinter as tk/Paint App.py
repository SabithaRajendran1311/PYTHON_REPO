import tkinter as tk
from tkinter import colorchooser
class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint")
        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack()
        self.color = "black"
        self.brush_size = 5
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()
        self.create_widgets()
        self.bind_events()
    def create_widgets(self):
        self.clear_button=tk.Button(self.button_frame,text="Clear",command=self.clear_canvas)
        self.clear_button.grid(row=0,column=0)
        self.color_button=tk.Button(self.button_frame,text="color",command=self.choose_color)
        self.color_button.grid(row=0,column=1)
        self.size_scale = tk.Scale(self.button_frame, from_=1, to=10, orient=tk.HORIZONTAL, label="Brush Size")
        self.size_scale.set(self.brush_size)
        self.size_scale.grid(row=0,column=2)
    def bind_events(self):
        self.canvas.bind("<B1-Motion>",self.paint)
    def paint(self,event):
        x1,y1=(event.x-self.brush_size),(event.y-self.brush_size)
        x2,y2=(event.x+self.brush_size),(event.y+self.brush_size)
        self.canvas.create_oval(x1,y1,x2,y2,fill=self.color,outline=self.color)
    def clear_canvas(self):
        self.canvas.delete("all")
    def choose_color(self):
        self.color = colorchooser.askcolor(color=self.color)[1]
root = tk.Tk()
paint_app = PaintApp(root)
root.mainloop()

