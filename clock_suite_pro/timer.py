import tkinter as tk


class Timer(tk.Frame):

    def __init__(self, parent):

        super().__init__(parent)


        self.remaining = 60

        self.running = False



        # 入力

        self.entry = tk.Entry(
            self,
            font=("Arial",20),
            width=10,
            justify="center"
        )

        self.entry.insert(
            0,
            "60"
        )

        self.entry.pack(
            pady=10
        )



        # 表示

        self.label = tk.Label(
            self,
            text="01:00",
            font=("Arial",35)
        )

        self.label.pack(
            pady=20
        )



        # ボタン

        tk.Button(
            self,
            text="開始",
            width=10,
            command=self.start
        ).pack()



        tk.Button(
            self,
            text="停止",
            width=10,
            command=self.stop
        ).pack()



        tk.Button(
            self,
            text="リセット",
            width=10,
            command=self.reset
        ).pack()



    def start(self):

        if not self.running:


            try:

                self.remaining = int(
                    self.entry.get()
                )

            except:

                self.remaining = 60



            self.running = True

            self.count()



    def count(self):

        if self.running and self.remaining >= 0:


            minutes = self.remaining // 60

            seconds = self.remaining % 60


            self.label.config(

                text=
                f"{minutes:02}:{seconds:02}"

            )


            self.remaining -= 1


            self.after(
                1000,
                self.count
            )



    def stop(self):

        self.running = False



    def reset(self):

        self.running = False

        self.remaining = 60

        self.label.config(
            text="01:00"
        )