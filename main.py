from cProfile import label
from textwrap import fill
from tkinter import *
import math
from urllib import response
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label.config(text="TIMER")
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        countdown(long_break_sec)
        label.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 1:
        countdown(work_sec)
        label.config(text="WORK", fg=GREEN)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label.config(text="BREAK", fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0"+str(count_sec)  # DP typing ,Python unique

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for i in range(work_session):
            marks += "✔"

        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=10, pady=10, bg=YELLOW)

# TIMER text
label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 64))
label.grid(row=0, column=1)

# tomato picture
canvas = Canvas(width=570, height=600, bg=YELLOW,
                highlightthickness=0)  # remove the border of tomato
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(285, 300, image=tomato_img)
timer_text = canvas.create_text(
    285, 340, text="00:00", fill="white", font=(FONT_NAME, 76, "bold"))
canvas.grid(row=1, column=1)

# start button
start = Button(text="Start", highlightthickness=10, command=start_timer)
start.grid(row=2, column=0)

# ✔
check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_marks.grid(row=2, column=1)

# end button
reset = Button(text="Reset", highlightthickness=10,command=reset_timer)
reset.grid(row=2, column=2)

window.mainloop()
