import tkinter as tk
from datetime import datetime, timedelta
class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.running = False
        self.start_time = None
        self.elapsed_time = timedelta()
        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.label.pack()
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT)
        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT)
        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT)
        self.update_clock()
    def start(self):
        if not self.running:
            self.start_time = datetime.now() - self.elapsed_time
            self.running = True
    def stop(self):
        if self.running:
            self.elapsed_time = datetime.now() - self.start_time
            self.running = False
    def reset(self):
        self.elapsed_time = timedelta()
        self.start_time = datetime.now()
        self.update_clock()
    def update_clock(self):
        if self.running:
            self.elapsed_time = datetime.now() - self.start_time
        time_str = str(self.elapsed_time).split(".")[0]
        self.label.config(text=time_str)
        self.root.after(50, self.update_clock)
root = tk.Tk()
root.title("Stopwatch")
Stopwatch = Stopwatch(root)
root.mainloop()

