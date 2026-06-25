import tkinter as tk
from datetime import datetime
import winsound


class Alarm(tk.Frame):

    def __init__(self,parent):

        super().__init__(parent)


        self.running = True


        self.entry = tk.Entry(
            self,
            font=("Arial",20),
            justify="center"
        )

        self.entry.insert(
            0,
            "21:00"
        )

        self.entry.pack(
            pady=10
        )



        self.label = tk.Label(
            self,
            text="設定中",
            font=("Arial",18)
        )

        self.label.pack()



        self.start_btn = tk.Button(
            self,
            text="開始",
            command=self.start
        )

        self.start_btn.pack()



        self.stop_btn = tk.Button(
            self,
            text="停止",
            command=self.stop
        )

        self.stop_btn.pack()



        self.check()



    def start(self):

        self.running = True

        self.label.config(
            text="アラーム設定中"
        )



    def stop(self):

        self.running = False

        self.label.config(
            text="停止中"
        )



    def check(self):

        if self.running:


            now = datetime.now().strftime(
                "%H:%M"
            )


            if now == self.entry.get():


                self.label.config(
                    text="⏰ アラーム時間です"
                )


                try:

                    winsound.Beep(
                        1000,
                        1000
                    )

                except:

                    pass



        self.after(
            1000,
            self.check
        )