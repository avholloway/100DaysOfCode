import os
import pandas
from tkinter import *
from random import choice

# === Global Constants =================================================================================================
DATA_FILE = "day31frenchwords.csv"
UNFAMILIAR_WORDS_FILE = "day30unfamiliarwords.csv"
BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT = "day31cardfront.png"
CARD_BACK = "day31cardback.png"

# === Global Variables =================================================================================================
finished = False
word_bank = None
current_word = None
card_timer = None

# === Read CSV File ====================================================================================================
def read_file():
    global word_bank
    try:
        df = pandas.read_csv(UNFAMILIAR_WORDS_FILE)
    except (FileNotFoundError, pandas.errors.EmptyDataError):
        df = pandas.read_csv(DATA_FILE)
    word_bank = df.to_dict(orient="records")

# === Get Random Word ==================================================================================================
def get_random_word():
    global card_timer
    if card_timer:
        window.after_cancel(card_timer)
    card_timer = window.after(3000, show_answer)
    return choice(word_bank)

# === Show Answer ======================================================================================================
def show_answer():
    card_can.itemconfig(language_text, text="English", fill="white")
    card_can.itemconfig(word_text, text=current_word["English"], fill="white")
    card_can.itemconfig(card, image=card_back_img)
    
# === Window ===========================================================================================================
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)
read_file()

# === Card Canvas ======================================================================================================
card_front_img = PhotoImage(file="day31cardfront.png")
card_back_img = PhotoImage(file="day31cardback.png")

card_can = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = card_can.create_image(400, 263, image=card_front_img)

current_word = get_random_word()

language_text = card_can.create_text(400, 150, text="French", fill="black", font=("Tebuchet MS", 40, "italic"))
word_text = card_can.create_text(400, 300, text=current_word["French"], fill="black", font=("Tebuchet MS", 60, "bold"))
card_can.grid(column=1, row=1, columnspan=2, pady=(0, 25))

card_timer = window.after(3000, show_answer)

# === Correct Mark Button ==============================================================================================
def finish():
    global finished, card_timer
    finished = True
    print(finished)
    card_can.itemconfig(language_text, text="Restarting in", fill="black")
    card_can.itemconfig(word_text, text="3 seconds...", fill="black")
    card_can.itemconfig(card, image=card_front_img)
    os.remove(UNFAMILIAR_WORDS_FILE)
    read_file()
    if card_timer:
        window.after_cancel(card_timer)
    card_timer = window.after(3000, restart)

def restart():
    global current_word
    current_word = get_random_word()
    card_can.itemconfig(language_text, text="French", fill="black")
    card_can.itemconfig(word_text, text=current_word["French"], fill="black")
    card_can.itemconfig(card, image=card_front_img)
    
def correct_on_click():
    global current_word
    if finished:
        return
    word_bank.remove(current_word)
    if len(word_bank) == 0:
        return finish()
    pandas.DataFrame(word_bank).to_csv(UNFAMILIAR_WORDS_FILE, index=False)
    current_word = get_random_word()
    card_can.itemconfig(language_text, text="French", fill="black")
    card_can.itemconfig(word_text, text=current_word["French"], fill="black")
    card_can.itemconfig(card, image=card_front_img)

correct_img = PhotoImage(file="right.png")
correct_button = Button(image=correct_img, width=98, height=98, bg=BACKGROUND_COLOR,
                        borderwidth=0, relief=FLAT, highlightthickness=0, command=correct_on_click)
correct_button.grid(column=1, row=2)

# === Wrong Mark Image =================================================================================================
def wrong_on_click():
    global current_word
    if finished:
        return
    if len(word_bank) == 0:
        return finish()
    current_word = get_random_word()
    card_can.itemconfig(language_text, text="French", fill="black")
    card_can.itemconfig(word_text, text=current_word["French"], fill="black")
    card_can.itemconfig(card, image=card_front_img)

wrong_img = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_img, width=98, height=98, bg=BACKGROUND_COLOR,
                      borderwidth=0, relief=FLAT, highlightthickness=0, command=wrong_on_click)
wrong_button.grid(column=2, row=2)

# === Program Loop =====================================================================================================
window.mainloop()
