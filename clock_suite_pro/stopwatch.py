
import tkinter as tk
import time

class Stopwatch(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.running=False
        self.start_time=0
        self.elapsed=0

        self.label=tk.Label(self,text="0.0",font=("Arial",30))
        self.label.pack(pady=20)

        tk.Button(self,text="開始",command=self.start).pack()
        tk.Button(self,text="停止",command=self.stop).pack()
        tk.Button(self,text="リセット",command=self.reset).pack()

    def start(self):
        self.running=True
        self.start_time=time.time()-self.elapsed
        self.loop()

    def loop(self):
        if self.running:
            self.elapsed=time.time()-self.start_time
            self.label.config(text=f"{self.elapsed:.1f}s")
            self.after(100,self.loop)

    def stop(self):
        self.running=False

    def reset(self):
        self.elapsed=0
        self.label.config(text="0.0")
