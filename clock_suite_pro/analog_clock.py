
import tkinter as tk
from datetime import datetime
import math

class AnalogClock(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.canvas=tk.Canvas(self,width=600,height=500,bg="#111")
        self.canvas.pack()
        self.update_clock()

    def update_clock(self):
        self.canvas.delete("all")
        cx,cy,r=300,250,180

        self.canvas.create_oval(
            cx-r,cy-r,cx+r,cy+r,
            outline="white",width=4
        )

        for n in range(1,13):
            a=math.radians(n*30-90)
            self.canvas.create_text(
                cx+(r-30)*math.cos(a),
                cy+(r-30)*math.sin(a),
                text=str(n),
                fill="white",
                font=("Arial",16)
            )

        now=datetime.now()

        hands=[
            ((now.hour%12)*30+now.minute*0.5,90,"cyan",7),
            (now.minute*6,130,"lime",5),
            (now.second*6,160,"red",2)
        ]

        for angle,length,color,width in hands:
            a=math.radians(angle-90)
            self.canvas.create_line(
                cx,cy,
                cx+length*math.cos(a),
                cy+length*math.sin(a),
                fill=color,width=width
            )

        self.after(1000,self.update_clock)
