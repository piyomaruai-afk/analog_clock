import tkinter as tk
from datetime import datetime
import math

# -----------------------------
# 設定
# -----------------------------

BG_COLOR = "#1e1e1e"
CLOCK_COLOR = "white"
SECOND_COLOR = "red"
MINUTE_COLOR = "#00ff99"
HOUR_COLOR = "#00ccff"

WIDTH = 600
HEIGHT = 700


# -----------------------------
# メイン
# -----------------------------

root = tk.Tk()
root.title("Analog Clock")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.configure(bg=BG_COLOR)

# 常に最前面
root.attributes("-topmost", True)


canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=500,
    bg=BG_COLOR,
    highlightthickness=0
)
canvas.pack()


digital_label = tk.Label(
    root,
    font=("Consolas", 24, "bold"),
    fg="#00ff99",
    bg=BG_COLOR
)
digital_label.pack(pady=10)


date_label = tk.Label(
    root,
    font=("Arial", 14),
    fg="white",
    bg=BG_COLOR
)
date_label.pack()


CENTER_X = WIDTH // 2
CENTER_Y = 250
RADIUS = 200


def draw_clock():

    canvas.delete("all")

    # 外枠
    canvas.create_oval(
        CENTER_X - RADIUS,
        CENTER_Y - RADIUS,
        CENTER_X + RADIUS,
        CENTER_Y + RADIUS,
        outline=CLOCK_COLOR,
        width=4
    )

    # 数字
    for num in range(1, 13):

        angle = math.radians(num * 30 - 90)

        x = CENTER_X + (RADIUS - 30) * math.cos(angle)
        y = CENTER_Y + (RADIUS - 30) * math.sin(angle)

        canvas.create_text(
            x,
            y,
            text=str(num),
            fill=CLOCK_COLOR,
            font=("Arial", 18, "bold")
        )


    now = datetime.now()

    hour = now.hour % 12
    minute = now.minute
    second = now.second


    # 時針
    hour_angle = math.radians(
        (hour * 30 + minute * 0.5) - 90
    )

    hour_x = CENTER_X + 90 * math.cos(hour_angle)
    hour_y = CENTER_Y + 90 * math.sin(hour_angle)

    canvas.create_line(
        CENTER_X,
        CENTER_Y,
        hour_x,
        hour_y,
        fill=HOUR_COLOR,
        width=8
    )


    # 分針
    minute_angle = math.radians(
        (minute * 6) - 90
    )

    minute_x = CENTER_X + 140 * math.cos(minute_angle)
    minute_y = CENTER_Y + 140 * math.sin(minute_angle)

    canvas.create_line(
        CENTER_X,
        CENTER_Y,
        minute_x,
        minute_y,
        fill=MINUTE_COLOR,
        width=5
    )


    # 秒針
    second_angle = math.radians(
        (second * 6) - 90
    )

    second_x = CENTER_X + 170 * math.cos(second_angle)
    second_y = CENTER_Y + 170 * math.sin(second_angle)

    canvas.create_line(
        CENTER_X,
        CENTER_Y,
        second_x,
        second_y,
        fill=SECOND_COLOR,
        width=2
    )


    # 中心
    canvas.create_oval(
        CENTER_X - 8,
        CENTER_Y - 8,
        CENTER_X + 8,
        CENTER_Y + 8,
        fill="white"
    )


    # デジタル時計
    digital_label.config(
        text=now.strftime("%H:%M:%S")
    )


    # 日付・曜日
    date_label.config(
        text=now.strftime("%Y/%m/%d (%A)")
    )


    root.after(1000, draw_clock)



# 起動
draw_clock()

root.mainloop()