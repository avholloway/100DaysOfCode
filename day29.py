import random
from tkinter import *
import pyperclip
from tkinter import messagebox

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_random_password():
    random.shuffle(letters)
    random.shuffle(numbers)
    random.shuffle(symbols)
    pw_letters = letters[:4]
    pw_numbers = numbers[:4]
    pw_symbols = symbols[:4]
    random_password = pw_letters + pw_numbers + pw_symbols
    random.shuffle(random_password)
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
label_font = ("Trebuchet MS", 10, "normal")
label1 = Label(text="Website:", font=label_font, bg="white")
label1.grid(column=1, row=2, pady=(0, 10), sticky="e")

# === Input Wedbsite ===================================================================================================
input1 = Entry(width=35, bg="#FBFBFB")
input1.grid(column=2, row=2, pady=(0, 10), columnspan=2, sticky="w")
input1.focus()

# === Label Email/Username =============================================================================================
label2 = Label(text="Email/Username:", font=label_font, bg="white")
label2.grid(column=1, row=3, pady=(0, 10), sticky="e")

# === Input Email/Username =============================================================================================
input2 = Entry(width=35, bg="#FBFBFB")
input2.grid(column=2, row=3, pady=(0, 10), columnspan=2, sticky="w")
input2.insert(END, "avholloway@gmail.com")

# === Label Password ===================================================================================================
label3 = Label(text="Password:", font=label_font, bg="white")
label3.grid(column=1, row=4, pady=(0, 10), sticky="e")

# === Input Password ===================================================================================================
input3 = Entry(width=24, bg="#FBFBFB")
input3.grid(column=2, row=4, pady=(0, 10), sticky="w")

# === Button Generate Password =========================================================================================
def button1_on_click():
    input3.delete(0, END)
    input3.insert(0, generate_random_password())

button1 = Button(text="Generate", relief=GROOVE, highlightthickness=0, command=button1_on_click)
button1.grid(column=3, row=4, pady=(0, 10), sticky="e")

# === Button Add Record ================================================================================================
def button2_on_click():
    website, id, password = input1.get(), input2.get(), input3.get()
    
    if not website or not id or not password:
        messagebox.showinfo(title="MyPass Input Validation", message="You need to fill in all fields.")
        return False
    
    with open("day29data.csv", "a") as f:
        f.write(f"{website},{id},{password}\n")
        
    input3.delete(0, END)
    input1.delete(0, END)
    input1.focus()
    
    pyperclip.copy(password)
    
button2 = Button(text="Save to Database", relief=GROOVE, highlightthickness=0, command=button2_on_click)
button2.grid(column=2, row=5, columnspan=2, pady=(0, 50), sticky="w")

# === Program Loop =====================================================================================================
window.mainloop()