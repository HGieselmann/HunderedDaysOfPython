import json
import random
import time
from tkinter import *
from tkinter import messagebox


def readJsonDict(filename):
    try:
        with open(filename, "r") as file:
            try:
                unknown_words = json.load(file)
            except KeyError as k:
                print(f"File exists, but could not read JSON data: \n{k}")
    except FileNotFoundError as e:
        print(f"Could not find data file for unknown words.\n{e}")
    finally:
        file.close()
    return unknown_words


def get_word():
    global current_key
    unknown_words = readJsonDict("unknown_words.json")
    keys = list(unknown_words.keys())
    try:
        key = random.choice(keys)
    except:
        messagebox.showinfo(title="Congratulations!", message="You knew all words, reseting the words!")
        known_words = readJsonDict("known_words.json")
        with open("unknown_words.json", "w") as file:
            json.dump(known_words, file, indent=4)
            print(known_words)
            file.close()
            current_key = random.choice(list(known_words.keys()))
            return current_key
    flashcard.config(text=f"German: \n{key}")
    window.update()
    time.sleep(3)
    flashcard.config(text=f"English: \n{unknown_words[key]}")
    return key


def correct_answer():
    global current_key
    unknown_words = readJsonDict("unknown_words.json")
    try:
        known_words = readJsonDict("known_words.json")
    except:
        known_words = {}
    print(current_key)
    new_entry = {current_key: unknown_words[current_key]}
    print(new_entry)
    known_words.update(new_entry)
    with open("known_words.json", "w") as file:
        json.dump(known_words, file, indent=4)
    unknown_words.pop(current_key, None)
    with open("unknown_words.json", 'w') as file:
        json.dump(unknown_words, file, indent=4)

    current_key = get_word()


def wrong_answer():
    print("You dead.")
    global current_key
    current_key = get_word()


window = Tk()
window.config(width=800, height=600)

flashcard = Label(width=20, height=10)
flashcard.grid(column=0, row=0, columnspan=3)

wrong = Button(text="wrong", width=25, command=wrong_answer)
wrong.grid(column=2, row=1)

correct = Button(text="correct", width=25, command=correct_answer)
correct.grid(column=0, row=1)
current_key = get_word()

window.mainloop()
