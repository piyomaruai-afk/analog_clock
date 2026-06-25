import tkinter as tk
from datetime import datetime
import math


# -----------------------------
# 設定
# -----------------------------

WIDTH = 600
HEIGHT = 550

BG_COLOR = "#111111"

CLOCK_COLOR = "white"
HOUR_COLOR = "cyan"
MINUTE_COLOR = "lime"
SECOND_COLOR = "red"


# -----------------------------
# アナログ時計
# -----------------------------

class AnalogClock(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.canvas = tk.Canvas(
            self,
            width=WIDTH,
            height=HEIGHT,
            bg=BG_COLOR,
            highlightthickness=0
        )

        self.canvas.pack()

        self.update_clock()


    def update_clock(self):

        self.canvas.delete("all")


        cx = WIDTH // 2
        cy = HEIGHT // 2 - 20

        r = 200


        # 時計外枠

        self.canvas.create_oval(
            cx-r,
            cy-r,
            cx+r,
            cy+r,
            outline=CLOCK_COLOR,
            width=4
        )


        # 目盛り

        for i in range(60):

            angle = math.radians(i * 6 - 90)

            if i % 5 == 0:
                length = 20
                width = 3
            else:
                length = 10
                width = 1


            x1 = cx + (r-5) * math.cos(angle)
            y1 = cy + (r-5) * math.sin(angle)

            x2 = cx + (r-length) * math.cos(angle)
            y2 = cy + (r-length) * math.sin(angle)


            self.canvas.create_line(
                x1,y1,
                x2,y2,
                fill=CLOCK_COLOR,
                width=width
            )



        # 数字

        for n in range(1,13):

            angle = math.radians(n*30-90)

            x = cx+(r-40)*math.cos(angle)
            y = cy+(r-40)*math.sin(angle)


            self.canvas.create_text(
                x,
                y,
                text=str(n),
                fill=CLOCK_COLOR,
                font=("Arial",18)
            )



        # 時刻取得

        now = datetime.now()



        # 針

        hands = [

            (
                (now.hour % 12) * 30
                + now.minute * 0.5,
                100,
                HOUR_COLOR,
                8
            ),


            (
                now.minute * 6,
                140,
                MINUTE_COLOR,
                5
            ),


            (
                now.second * 6,
                170,
                SECOND_COLOR,
                2
            )

        ]



        for angle,length,color,width in hands:


            rad = math.radians(angle-90)


            self.canvas.create_line(

                cx,
                cy,

                cx + length * math.cos(rad),

                cy + length * math.sin(rad),

                fill=color,

                width=width

            )



        # 中央部分

        self.canvas.create_oval(

            cx-8,
            cy-8,

            cx+8,
            cy+8,

            fill="white"

        )



        # 日付表示

        self.canvas.create_text(

            cx,

            cy+r+45,

            text=now.strftime(
                "%Y/%m/%d  %H:%M:%S"
            ),

            fill="white",

            font=("Arial",18)

        )



        # 100ms更新

        self.after(
            100,
            self.update_clock
        )



# -----------------------------
# 起動
# -----------------------------

if __name__ == "__main__":

    root = tk.Tk()

    root.title(
        "Python Analog Clock"
    )

    root.resizable(
        False,
        False
    )


    clock = AnalogClock(root)

    clock.pack()


    root.mainloop()