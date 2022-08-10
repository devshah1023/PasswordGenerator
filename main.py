import tkinter as tk

import pyperclip

import random


root = tk.Tk()
root.title("Password Generator")

passlen = tk.IntVar()

# setting the length of the password to zero initially
passlen.set(0)


def password_generator():

    # write a for loop that goes from length 0 to specified length of password and randomly chooses a character
    # from the list above and append it to a string which is the password

    passwordKey = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
                   '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    password = ""
    for i in range(passlen.get()):
        password += random.choice(passwordKey)

    tk.Label(root, text=password).pack()
    pyperclip.copy(password)


tk.Label(root, text="Enter password length: ").pack()
entry1 = tk.Entry(root, textvariable=passlen)
entry1.pack()


tk.Button(root, text="Generate Password",
          command=password_generator).pack()

tk.Label(root, text="Your password will be copied to clipboard automatically!").pack()


root.mainloop()
