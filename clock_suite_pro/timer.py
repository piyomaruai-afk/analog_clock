
import tkinter as tk

class Timer(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.sec=60

        self.label=tk.Label(self,text="60",font=("Arial",30))
        self.label.pack(pady=20)

        tk.Button(self,text="開始",command=self.start).pack()

    def start(self):
        self.count()

    def count(self):
        if self.sec>=0:
            self.label.config(text=str(self.sec))
            self.sec-=1
            self.after(1000,self.count)
