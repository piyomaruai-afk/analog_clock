import tkinter as tk
import time


class Stopwatch(tk.Frame):

    def __init__(self, parent):

        super().__init__(parent)


        # 状態管理

        self.running = False

        self.start_time = 0

        self.elapsed = 0

        self.laps = []



        # 時間表示

        self.label = tk.Label(
            self,
            text="00:00:00.000",
            font=("Arial", 32)
        )

        self.label.pack(pady=20)



        # ボタンエリア

        button_frame = tk.Frame(self)

        button_frame.pack()



        self.start_btn = tk.Button(
            button_frame,
            text="開始",
            width=10,
            command=self.start
        )

        self.start_btn.grid(
            row=0,
            column=0,
            padx=5
        )



        self.stop_btn = tk.Button(
            button_frame,
            text="停止",
            width=10,
            command=self.stop
        )

        self.stop_btn.grid(
            row=0,
            column=1,
            padx=5
        )



        self.reset_btn = tk.Button(
            button_frame,
            text="リセット",
            width=10,
            command=self.reset
        )

        self.reset_btn.grid(
            row=0,
            column=2,
            padx=5
        )



        self.lap_btn = tk.Button(
            button_frame,
            text="ラップ",
            width=10,
            command=self.lap
        )

        self.lap_btn.grid(
            row=0,
            column=3,
            padx=5
        )



        # ラップ表示

        tk.Label(
            self,
            text="Lap Time"
        ).pack()



        self.lap_list = tk.Listbox(
            self,
            width=30,
            height=10
        )

        self.lap_list.pack(
            pady=10
        )



        self.best_label = tk.Label(
            self,
            text="Best: --"
        )

        self.best_label.pack()



    # 開始

    def start(self):

        if not self.running:

            self.running = True


            self.start_time = (
                time.perf_counter()
                - self.elapsed
            )


            self.update()



    # 更新

    def update(self):

        if self.running:


            self.elapsed = (
                time.perf_counter()
                - self.start_time
            )


            self.display_time()


            self.after(
                10,
                self.update
            )



    # 表示

    def display_time(self):

        ms = int(
            (self.elapsed % 1)
            * 1000
        )


        sec = int(
            self.elapsed
        )


        minutes = sec // 60

        seconds = sec % 60



        self.label.config(
            text=
            f"{minutes:02}:{seconds:02}:{ms:03}"
        )



    # 停止

    def stop(self):

        self.running = False



    # リセット

    def reset(self):

        self.running = False

        self.elapsed = 0

        self.laps.clear()


        self.lap_list.delete(
            0,
            tk.END
        )


        self.best_label.config(
            text="Best: --"
        )


        self.display_time()



    # ラップ

    def lap(self):

        if self.running:


            lap_time = self.elapsed


            self.laps.append(
                lap_time
            )


            self.lap_list.insert(
                tk.END,
                f"Lap {len(self.laps)}  "
                f"{self.format_time(lap_time)}"
            )


            self.update_best()



    # ベストラップ

    def update_best(self):

        best = min(
            self.laps
        )


        self.best_label.config(
            text=
            "Best: "
            + self.format_time(best)
        )



    # 時間整形

    def format_time(self,t):

        ms = int(
            (t % 1)
            * 1000
        )


        sec = int(t)


        return (
            f"{sec//60:02}:"
            f"{sec%60:02}:"
            f"{ms:03}"
        )