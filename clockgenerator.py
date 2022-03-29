import tkinter as ui
import time

import math

window = ui.Tk()
window.geometry("400x400")


def update_clock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%s"))

    seconds_x = seconds_hand_len * __math.sin(math.radians(seconds * 6))+center_x
    seconds_y = -1 * seconds_hand_len * math.cos(math.radians(seconds * 6)) + center_y
    canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)

    window.after(1000, update_clock)

    canvas = ui.Canvas(window, width=400, height=400, bg="black")
    canvas.pack(expand=True, fill='both')