import tkinter as tk
from datetime import datetime
from zoneinfo import ZoneInfo


class WorldClock(tk.Frame):

    def __init__(self,parent):

        super().__init__(parent)


        self.clocks = {

            "Japan":
                "Asia/Tokyo",

            "London":
                "Europe/London",

            "New York":
                "America/New_York",

            "Sydney":
                "Australia/Sydney"

        }


        self.labels = {}


        for city in self.clocks:

            label = tk.Label(
                self,
                font=("Arial",18),
                justify="left"
            )

            label.pack(
                pady=5
            )

            self.labels[city] = label


        self.update_clock()



    def update_clock(self):


        for city,zone in self.clocks.items():


            now = datetime.now(
                ZoneInfo(zone)
            )


            self.labels[city].config(

                text=
                f"{city}\n"
                f"{now.strftime('%Y/%m/%d %H:%M:%S')}"

            )


        self.after(
            1000,
            self.update_clock
        )