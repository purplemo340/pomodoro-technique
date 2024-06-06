from tkinter import *
import math
#color hunt for colors
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
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global timer
    check.config(text="")
    window.after_cancel(timer)
    title.config(text="Timer", fg=GREEN)
    reps=0
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1
    if reps%8 == 0:
        countdown(LONG_BREAK_MIN*60)
    elif reps % 2 == 1:
        countdown(WORK_MIN*60)
        title.config(text="Work", fg=RED)
    else:
        countdown(SHORT_BREAK_MIN*60)
        title.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    global timer
    sec=count%60
    if sec==0:
        sec="00"
    elif sec<10 and sec!=0:
        sec=f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{math.floor(count/60)}:{sec}")
    if count>0:
        timer=window.after(1000, countdown, count-1)
    else:
        start()
        if reps%2==0:
             check['text']+=("✔")
# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

fg = GREEN
title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
title.grid(column=1, row=0)

canvas=Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text=canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_s=Button(text="Start", command=start)
button_s.grid(column=0, row=2)

button_r=Button(text="Reset", command=reset)
button_r.grid(column=2, row=2)

check=Label( bg=YELLOW)
check.grid(column=1, row=3)

window.mainloop()