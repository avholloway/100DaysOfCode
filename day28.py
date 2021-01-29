from tkinter import *

# === Constants ========================================================================================================
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Trebuchet MS"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
cycles = [WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, LONG_BREAK_MIN]
cycle_number = 0
progress_incomplete = "▫"
progress_complete = "▪"
running = False
timer = None

# === Timer Start Functionality  =======================================================================================
def start_timer():
    global running
    
    running = True
    cycle_number = 0
    label1.config(text="Work Time")
    label2.config(text=f"{progress_complete}{progress_incomplete * 3}")
    count_down(cycles[cycle_number] * 60)
    
def button1_on_click():
    reset_timer()
    start_timer()


# === Timer Countdown Functionality ====================================================================================
def count_down(count):
    global timer, cycle_number
    
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
    
    
    if count == 0:
        
        # a cycle count down just finished, move to next cycle
        cycle_number += 1
        
        if running and cycle_number < len(cycles) - 1:
            count_down(cycles[cycle_number] * 60)
        
        # was it a work (even) or break (odd) cycle?
        if cycle_number % 2 == 0:
            label2.config(
                text=f"{progress_complete * (cycle_number // 2 + 1)}{progress_incomplete * (4 - (cycle_number // 2 + 1))}")
            label1.config(text="Work Time")
        else:
            label1.config(text="Break Time")
            
    else:
        
        # we're in the middle of a countdown
        if running:
            timer = window.after(1000, count_down, count - 1)

# === Timer Reset Functionality ========================================================================================
def reset_timer():
    global cycle_number, running
    
    try:
        window.after_cancel(timer)
    except:
        pass
    running = False
    cycle_number = 0
    label1.config(text="Timer")
    label2.config(text=progress_incomplete * 4)
    canvas.itemconfig(timer_text, text=f"00:00")
    
def button2_on_click():
    reset_timer()
    
# === Window ===========================================================================================================
window = Tk()
window.config(padx=10, pady=10, bg=YELLOW)
window.title("Pomodoro")

# === Label Title ======================================================================================================
label_font = (FONT_NAME, 28, "bold")
label1 = Label(text="Timer", font=label_font, bg=YELLOW, fg=GREEN)
label1.grid(columnspan=3, column=1, row=1, pady=(10, 0))

# === Canvas Timer =====================================================================================================
tomato_image = PhotoImage(file="day28tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(columnspan=3, column=1, row=2, padx=40)

# === Button 1 Start ===================================================================================================
button1 = Button(text="Start", relief=GROOVE, highlightthickness=0, command=button1_on_click)
button1.grid(column=1, row=3, pady=(20, 20))

# === Label Progress ===================================================================================================
label_font = (FONT_NAME, 36, "bold")
label2 = Label(text=progress_incomplete * 4, font=label_font, bg=YELLOW, fg=GREEN)
label2.grid(column=2, row=3, pady=(20, 20))

# === Button 2 Reset ===================================================================================================
button2 = Button(text="Reset", relief=GROOVE, highlightthickness=0, command=button2_on_click)
button2.grid(column=3, row=3, pady=(20, 20))

# === Program Loop =====================================================================================================
window.mainloop()