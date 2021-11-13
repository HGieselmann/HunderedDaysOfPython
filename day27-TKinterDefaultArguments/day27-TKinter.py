from tkinter import *

def button_clicked():
    print(f"Button clicked.")
    new_text = input.get()
    title_label["text"] = new_text

window = Tk()
window.title("Super GUI")
window.minsize(width=640, height=480)

title_label = Label(text="Super GUI", font=("Courier", 16, "bold"))
# We can provide additional arguments, but all defaults are set, example see above
title_label.pack(side="top")

sub_label = Label(text="Sub-Label", font=("Courier", 10, 'normal'))
sub_label.place(x=20, y= 20)



button = Button(text="Click me", command=button_clicked)
button.place(x=100, y = 20)

input = Entry()
input.pack()






window.mainloop()
