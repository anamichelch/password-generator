import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    p_letters = [choice(letters) for letter in range(randint(8, 10))]
    p_numbers = [choice(numbers) for number in range(randint(2, 4))]
    p_symbols = [choice(symbols) for symbol in range(randint(2, 4))]

    password_list = p_letters + p_numbers + p_symbols
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }}
    if len(website) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showinfo("Oops", message="Please don't leave any fields empty!")
    else:
        with open("passwords.json", "r") as file:

            try:
                data = json.load(file)
            except FileNotFoundError:
                with open("passwords.json", "w") as file:
                    json.dump(data, file, indent=4)
            else:
                data.update(new_data)
                with open("passwords.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- LOOK FOR PASSWORD --------------------------- #

def search_password():
    website = website_entry.get()
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message= "No data file yet")
    else:
        if website in data:
            messagebox.showinfo(title=website ,message=f"Email: {data[website]['email']}\n Password: {data[website]['password']}")
        else:
            messagebox.showinfo("Ooops!","Sorry, you dont have data for this website")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

FONT = ("Ariel", 8)

# labels
website_lbl = Label(text="Website: ", font=FONT)
website_lbl.grid(column=0, row=1)

email_lbl = Label(text="Email or Username: ", font=FONT)
email_lbl.grid(column=0, row=2)

password_lbl = Label(text="Password: ", font=FONT)
password_lbl.grid(column=0, row=3)

# Entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, sticky="EW")

email_entry = Entry(width=35)
email_entry.grid(columnspan=2, column=1, row=2, sticky="EW")
email_entry.insert(0, "ana.michelc13@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
add_button = Button(text="Add", font=FONT, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

generate_button = Button(text="Generate Password", width=15, font=FONT, command=generate_password)
generate_button.grid(column=2, row=3, sticky="EW")

search_button = (Button(text="Search", font=FONT, width=15, command=search_password))
search_button.grid(column=2, row=1)
window.mainloop()
