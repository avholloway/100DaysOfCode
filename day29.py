import pyperclip
from tkinter import *
from random import shuffle
from tkinter import messagebox
from collections import namedtuple
import sys

# === Global Constants =================================================================================================
Font = namedtuple("Font", ("family", "size", "style"))
BASE_FONT = Font("Trebuchet MS", 12, "normal")
LABEL_FONT = Font(BASE_FONT.family, 10, BASE_FONT.style)
INPUT_FONT = Font(BASE_FONT.family, 10, BASE_FONT.style)
BUTTON_FONT = Font(BASE_FONT.family, 8, BASE_FONT.style)

# === Password Generator ===============================================================================================
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_random_password():
    # shuffle the starting positions of our character sets
    shuffle(letters)
    shuffle(numbers)
    shuffle(symbols)
    
    # grab some lower case letters
    pw_letters_lower = letters[:2]
    
    # grab some upper case letters
    shuffle(letters)
    pw_letters_upper = [letter.upper() for letter in letters][:2]
    
    # some numbers
    pw_numbers = numbers[:4]
    
    # And some symbols
    pw_symbols = symbols[:4]
    
    # put it all in one big list of chars
    random_password = pw_letters_lower + pw_letters_upper + pw_numbers + pw_symbols
    
    # give it a good shake
    shuffle(random_password)
    
    # and viola, a new password is born!
    return ''.join(random_password)

# === Window ===========================================================================================================
window = Tk()
window.title("MyPass")
window.config(bg="white")
window.config(padx=60)

# === Canvas Logo ======================================================================================================
logo = PhotoImage(file="day29logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=1, columnspan=3, pady=(12, 25))

# === Label Website ====================================================================================================
label1 = Label(text="Website:", font=LABEL_FONT, bg="white")
label1.grid(column=1, row=2, pady=(0, 10), sticky="e")

# === Input Website ===================================================================================================
input1 = Entry(width=35, font=INPUT_FONT, bg="#FBFBFB")
input1.grid(column=2, row=2, pady=(0, 10), columnspan=2, sticky="w")
input1.focus()

# === Label Email/Username =============================================================================================
label2 = Label(text="Email/Username:", font=LABEL_FONT, bg="white")
label2.grid(column=1, row=3, pady=(0, 10), sticky="e")

# === Input Email/Username =============================================================================================
input2 = Entry(width=35, font=INPUT_FONT, bg="#FBFBFB")
input2.grid(column=2, row=3, pady=(0, 10), columnspan=2, sticky="w")
input2.insert(END, "avholloway@gmail.com")

# === Label Password ===================================================================================================
label3 = Label(text="Password:", font=LABEL_FONT, bg="white")
label3.grid(column=1, row=4, pady=(0, 10), sticky="e")

# === Input Password ===================================================================================================
input3 = Entry(width=24, font=INPUT_FONT, bg="#FBFBFB")
input3.grid(column=2, row=4, pady=(0, 10), sticky="w")

# === Button Generate Password =========================================================================================
def button1_on_click():
    input3.delete(0, END)
    input3.insert(0, generate_random_password())

button1 = Button(text=" Generate ", font=BUTTON_FONT, relief=GROOVE, highlightthickness=0, command=button1_on_click)
button1.grid(column=3, row=4, pady=(0, 10), sticky="e")

# === Button Add Record ================================================================================================
def button2_on_click():
    website, id, password = input1.get(), input2.get(), input3.get()
    
    if not website or not id or not password:
        messagebox.showinfo(title="MyPass Input Validation", message="All fields required.")
        return False
    
    with open("day29data.csv", "a") as f:
        f.write(f"{website},{id},{password}\n")
        
    input3.delete(0, END)
    input1.delete(0, END)
    input1.focus()
    
    pyperclip.copy(password)
    
button2 = Button(text=" Save to Database ", font=BUTTON_FONT, relief=GROOVE, highlightthickness=0, command=button2_on_click)
button2.grid(column=2, row=5, columnspan=2, pady=(0, 50), sticky="w")

# === Program Loop =====================================================================================================
window.mainloop()