import tkinter as tk
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
def resetTimer():
    window.after_cancel()
    canvas.itemconfig(timerText, text=f"00:00")
    title.config(text="Timer", fg=GREEN)
    checkMarks.config(text="")
    global reps 
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    global reps
    reps += 1
        
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN*60)
        title.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN*60)
        title.config(text="Short Break", fg=PINK)
    else: 
        countdown(WORK_MIN*60)
        title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    newCountMins = int(count / 60)
    newCountSecs = int(count % 60)
    
    if newCountSecs < 10:
        newCountSecs = f"0{newCountSecs}"
    
    canvas.itemconfig(timerText, text=f"{newCountMins}:{newCountSecs}")
    
    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        startTimer()
        marks = ""
        for _ in range(reps//2):
            marks+="✔"

        checkMarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro - \"Italian for Tomato\"")
window.config(padx=100,pady=100,bg=YELLOW)



title = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold") )
title.grid(column=1,row=0)

canvas = tk.Canvas(width=200,height=224,bg=YELLOW, bd=0, highlightthickness=0, relief='ridge')
photo = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timerText = canvas.create_text(100, 130, text="0:00", fill="white", font=(FONT_NAME, 35,"bold"))
canvas.grid(column=1,row=1)

startTimer = tk.Button(text="Start",highlightthickness=0, command=startTimer)
startTimer.grid(column=0,row=2)

resetTimer = tk.Button(text="Reset",highlightthickness=0, command=resetTimer)
resetTimer.grid(column=2,row=2)

checkMarks = tk.Label(text="", fg=GREEN, bg=YELLOW)
checkMarks.grid(column=1,row=3)


window.mainloop()