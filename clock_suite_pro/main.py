
import tkinter as tk
from tkinter import ttk
from analog_clock import AnalogClock
from stopwatch import Stopwatch
from timer import Timer
from alarm import Alarm
from world_clock import WorldClock
from theme import ThemeManager

root = tk.Tk()
root.title("Clock Suite Pro")
root.geometry("950x750")

theme = ThemeManager(root)

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

for app, name in [
    (AnalogClock, "時計"),
    (Stopwatch, "ストップウォッチ"),
    (Timer, "タイマー"),
    (Alarm, "アラーム"),
    (WorldClock, "世界時計")
]:
    notebook.add(app(notebook), text=name)

tk.Button(
    root,
    text="ライト/ダーク切替",
    command=theme.toggle
).pack(pady=5)

root.mainloop()
