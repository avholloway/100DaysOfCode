import tkinter

# === Window ===========================================================================================================
window = tkinter.Tk()
window.minsize(width=500, height=300)
window.title("My Window")
window.config(padx=10, pady=10)

# === Label ============================================================================================================
label_font = ("Trebuchet MS", 16, "normal")
label1 = tkinter.Label(text="Label1", font=label_font)
label1.grid(column=1, row=1)
label1.config(padx=0, pady=40)

# === Button ===========================================================================================================
def button1_on_click():
    print(f"{input1.get()=}")
    label1["text"] = input1.get()

button1 = tkinter.Button(text="Click Me", command=button1_on_click)
button1.grid(column=1, row=2)

# === Input ============================================================================================================
input1 = tkinter.Entry(width=10)
input1.grid(column=2, row=2)

# === Text =============================================================================================================
text1 = tkinter.Text(width=30, height=5)
text1.insert(tkinter.END, "Yo")
text1.grid(column=3, row=3)

# === Spin Box =========================================================================================================
def spin1_on_use():
    print(f"{spin1.get()=}")
    
spin1 = tkinter.Spinbox(from_=0, to=10, width=5, command=spin1_on_use)
spin1.grid(column=1, row=4)

# === Scale ============================================================================================================
def scale1_on_use(scale1_value):
    print(f"{scale1_value=}")
    
scale1 = tkinter.Scale(from_=0, to=100, command=scale1_on_use)
scale1.grid(column=2, row=4)

# === Checkbox =========================================================================================================
def checkbox1_on_change():
    print(f"{checkbox1_state.get()=}")
    
checkbox1_state = tkinter.IntVar()
checkbox1 = tkinter.Checkbutton(text="Break?", variable=checkbox1_state, command=checkbox1_on_change)
checkbox1.grid(column=3, row=4)

# === Radio Button =====================================================================================================
def radio1_on_change():
    print(f"{radio1_state.get()=}")
    
radio1_state = tkinter.IntVar()
radio1a = tkinter.Radiobutton(text="Male", value=1, variable=radio1_state, command=radio1_on_change)
radio1b = tkinter.Radiobutton(text="Female", value=2, variable=radio1_state, command=radio1_on_change)
radio1a.grid(column=4, row=4)
radio1b.grid(column=5, row=4)

# === List Box =========================================================================================================
list1 = tkinter.Listbox(height=3)

def list1_used(event):
    print(f"{list1.get(list1.curselection())=}")
    
for index, item in enumerate(["apple", "banana", "pear"]):
    list1.insert(index, item)
    
list1.bind("<<ListboxSelect>>", list1_used)
list1.grid(column=1, row=5)

# === Window Main Loop =================================================================================================
window.mainloop()