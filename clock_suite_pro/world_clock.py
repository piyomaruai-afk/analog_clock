
import tkinter as tk
from datetime import datetime, timezone

class WorldClock(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.label=tk.Label(
            self,
            font=("Arial",20)
        )
        self.label.pack(pady=30)

        self.update()

    def update(self):
        utc=datetime.now(timezone.utc)

        self.label.config(
            text=f"UTC\n{utc.strftime('%H:%M:%S')}"
        )

        self.after(1000,self.update)
