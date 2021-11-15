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


def add_password():
    if len(website_input.get()) < 1 or len(password_input.get()) < 1:
        messagebox.showinfo(title="Info incomplete", message="Please enter all fields!")
        return

    answer = messagebox.askokcancel(title="Is this correct?", message=f"Website: {website_input.get()} \n"
                                                             f"Username: {username_input.get()} \n"
                                                             f"Password: {password_input.get()} ")
    if answer:
        with open("data.txt", "a") as file:
            file.write(f"{website_input.get()}, {username_input.get()}, {password_input.get()}\n")
            file.close()
        website_input.delete(0, END)
        password_input.delete(0, END)
        print("Added Password to file")


window = Tk()
window.title("My Password Manager")
window.config(padx=20, pady=20)

logo = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website = Label(width=0, text="Website")
website.grid(column=0, row=1)
website_input = Entry(width=52)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

username = Label(width=0, text="Username/Password")
username.grid(column=0, row=2)
username_input = Entry(width=52)
username_input.insert(0, "example@mail.com")
username_input.grid(column=1, row=2, columnspan=2)

password = Label(width=0, text="Password")
password.grid(column=0, row=3)
password_input = Entry(width=32)
password_input.grid(column=1, row=3)
password_generate= Button(text="Generate Password", command=generate_password)
password_generate.grid(column=2, row=3)

add_button = Button(text="Add", width=60, command=add_password)
add_button.grid(column=0, row=4, columnspan=3)


window.mainloop()
