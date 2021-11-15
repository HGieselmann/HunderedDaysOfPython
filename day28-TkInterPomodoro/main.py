import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    # This works, because we can dynamically change the data-type of a variable
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PyPomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


def say_something(thing):
    print(thing)


window.after(100, say_something, "Hellooo")

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, 'bold'))
label.grid(column=1, row=0)

start_button = Button(text="Start", padx=10, pady=2, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", padx=10, pady=2, command=reset_timer)
reset_button.grid(column=2, row=2)

canvas = Canvas(width=230, height=220, bg=YELLOW, highlightthickness=0)

image = PhotoImage(file="tomato.png")
canvas.create_image(115, 108, image=image)
timer_text = canvas.create_text(115, 125, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
