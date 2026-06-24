
import tkinter as tk
from datetime import datetime

class Alarm(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.entry=tk.Entry(self)
        self.entry.insert(0,"21:00")
        self.entry.pack(pady=10)

        self.label=tk.Label(self,text="")
        self.label.pack()

        self.check()

    def check(self):
        now=datetime.now().strftime("%H:%M")

        if now==self.entry.get():
            self.label.config(text="アラーム時間です")

        self.after(1000,self.check)
