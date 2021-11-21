import pretty_errors
from rich import print

import json
from tkinter import *
from tkinter import messagebox
import pyperclip


def generate_password():
    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list = [random.choice(letters) for x in range(nr_letters)]
    password_list.extend([random.choice(symbols) for x in range(nr_symbols)])
    password_list.extend([random.choice(numbers) for x in range(nr_numbers)])

    random.shuffle(password_list)

    new_password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, new_password)
    pyperclip.copy(new_password)
    return new_password


def search_library():
    print("[magenta]Looking for password...[/magenta]")
    try:
        with open("data.json") as file:
            password_dict = json.load(file)
    except FileNotFoundError as error:
        messagebox.showinfo(title="Library not found", message="No library file found.")
    finally:
        file.close()

    page_to_find = website_input.get()
    for key in password_dict:
        if key == page_to_find:
            messagebox.showinfo(title=page_to_find,
                                message=f"Website: {page_to_find}\n username:{password_dict[key]['email']} \nPassword:{password_dict[key]['password']}")
            return

    messagebox.showinfo(title="Could not find a match.", message="There was not matching pair in the library.")



def add_password():
    if len(website_input.get()) < 1 or len(password_input.get()) < 1:
        messagebox.showinfo(title="Info incomplete", message="Please enter all fields!")
        return

    answer = messagebox.askokcancel(title="Is this correct?", message=f"Website: {website_input.get()} \n"
                                                                      f"Username: {username_input.get()} \n"
                                                                      f"Password: {password_input.get()} ")
    if answer:
        new_data = {
            website_input.get(): {
                "email": username_input.get(),
                "password": password_input.get()

            }
        }
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
                print("Added Password to file")
        except:
            print("Did not find a library file, creating a new one!")
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            file.close()


window = Tk()
window.title("My Password Manager")
window.config(padx=20, pady=20)

logo = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website = Label(width=0, text="Website")
website.grid(column=0, row=1)
website_input = Entry(width=32)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=1)

search_btn = Button(text="search", width=15, command=search_library)
search_btn.grid(column=2, row=1, columnspan=1)

username = Label(width=0, text="Username/Password")
username.grid(column=0, row=2)
username_input = Entry(width=52)
username_input.insert(0, "example@mail.com")
username_input.grid(column=1, row=2, columnspan=2)

password = Label(width=0, text="Password")
password.grid(column=0, row=3)
password_input = Entry(width=32)
password_input.grid(column=1, row=3)
password_generate = Button(text="Generate Password", command=generate_password)
password_generate.grid(column=2, row=3)

add_button = Button(text="Add", width=60, command=add_password)
add_button.grid(column=0, row=4, columnspan=3)

window.mainloop()
