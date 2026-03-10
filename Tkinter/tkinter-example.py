import tkinter as tk
import tkinter.font as tfont
import tkinter.ttk as ttk

# TK >> This is class. It created a window

window = tk.Tk()
window.title("My Window")
window.minsize(400, 300)

custom_font = tfont.Font(family="Helvetica", weight="bold", size=15)

label1 = ttk.Label(window, text="My First App", font=custom_font)
label1.pack(pady=10)
# label1["text"] = "My First"
# label1.config(text="hello world")

# <<<<< INPUT >>>>
user_input = ttk.Entry()
user_input.pack()
user_input.get()



# <<<< BUTTON  >>>>
# counter = 0
def funct_button():
    # global counter
    input_text = user_input.get()
    label1.config(text=f"you typed: {input_text}")
    # counter += 1

button1 = ttk.Button(text="Click", command = funct_button )
button1.pack(pady=10)

# Seprator
sep = ttk.Separator(orient="horizontal" )
sep.pack(fill = "x")


# Taking input from users

text = tk.Text(width=20, height=10)
text.pack(pady=10)
text.focus() # to bring curson in the box bu default
text.insert("1.0", "Enter TEXT")

text.get("1.0", "end")

def funct_button_submit():
    submit = text.get("1.0", "end")
    print(f"The typed text is: {submit}")
button_submit = ttk.Button(text="Submit", command=funct_button_submit)
button_submit.pack()

# text["state"] = "disabled"
# def funct_button2():
#     text["state"] = "normal"
#
# enable_btn = ttk.Button(text="Enable", command=funct_button2)
# enable_btn.pack()

# check button

# check_option = tk.IntVar() # for one and zero
check_option = tk.StringVar()

def check_option_task():
    print(check_option.get())
check_button = ttk.Checkbutton(text="Agree with terms and condition", variable=check_option, command=check_option_task,
                               onvalue="Yes", offvalue="NO")
check_button.pack()

radio_value = tk.StringVar()

def radio_option_task():
    print(radio_value.get())

option1= ttk.Radiobutton(text="Male", variable=radio_value, value="male", command=radio_option_task)
option2= ttk.Radiobutton(text="Female", variable=radio_value, value="female", command=radio_option_task)

option1.pack()
option2.pack()

# Combo box: Drop down box

selected_countries = tk.StringVar()
countries = ttk.Combobox(textvariable=selected_countries, values=("Australia", "Canada", "India", "Sweden", "US"))
countries["state"] = "readonly"
countries.pack()

labelcont= ttk.Label()
labelcont.pack()

def display_contry(event):
    labelcont.config(text=f"Selected country is: {selected_countries.get()}")
    # print(f"selected contry is {selected_countries.get()}")

countries.bind("<<ComboboxSelected>>", display_contry)  # this is the even which passes the selected items as even to function

# List Box
food_items = ("Pizza", "Burger", "garlic Bread", "nachos", "Salad")
fav_food = tk.StringVar(value=food_items)

food_list=tk.Listbox(listvariable=fav_food, height=5, selectmode="multiple")
food_list.pack()

def display_food(event):
    food_index = food_list.curselection()
    for i in food_index:
        print(food_list.get(i))

food_list.bind("<<ListboxSelect>>", display_food)


# Spinbox: counter to increase or decrease a value
counter1 = tk.IntVar(value=10)

def spin_box():
    print(spin_box.get())

spin_box = ttk.Spinbox(from_=0, to=20, textvariable=counter1, wrap=True, command=spin_box)
spin_box.pack()



print(spin_box.get())


# <<<< Quit Or Destroy >>>>>
quitbutton = ttk.Button(window, text="QUIT", command=window.destroy)
quitbutton.pack(pady=10)

window.mainloop()