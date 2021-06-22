import tkinter as tk
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', "&", '(', ')', '*', '+'] 

    passwordLetters = [random.choice(letters) for _ in range(random.randint(8,10))]
    passwordSymbols = [random.choice(symbols) for _ in range(random.randint(2,4))]
    passwordNumbers = [random.choice(numbers) for _ in range(random.randint(2,4))]

    password = passwordLetters + passwordSymbols + passwordNumbers 
    random.shuffle(password)
    passwordString = "".join(password)

    passwordInput.delete(0, 'end')
    passwordInput.insert(0, f"{passwordString}")





# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePassword():
    websiteName = websiteInput.get()
    username = usernameInput.get()
    password = passwordInput.get()

    if len(username) == 0 or len(password) == 0 or len(websiteName) == 0:
        messagebox.showinfo(title="Oops", message="Please fill out all fields")
        return

    isOK = messagebox.askokcancel(title=websiteName, message = f"These are the details entered: \n\nEmail: {username} \nPassword: {password} \n\nIs this information ok to save?")
    
    if isOK:
        with open('data.txt', 'a') as file:    
            file.write(f"{websiteName} | {username} | {password}\n")
            websiteInput.delete(0, 'end')
            usernameInput.delete(0, 'end')
            usernameInput.insert(0, "BrentLittlefield@email.com")
            passwordInput.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1,row=0)

websiteLabel    = tk.Label(text="Website:")
websiteInput    = tk.Entry(width=35)
usernameLabel   = tk.Label(text="Email/Username:")
usernameInput   = tk.Entry(width=35)
passwordLabel   = tk.Label(text="Password:")
passwordInput   = tk.Entry(width=21)
passwordButton  = tk.Button(text="Generate Password", command=generatePassword)
addButton       = tk.Button(text="Add", width=36, command=savePassword)

usernameInput.insert(0,"BrentLittlefield@email.com")

websiteLabel.grid(column=0,row=1)
websiteInput.grid(column=1,row=1,columnspan=2)
usernameLabel.grid(column=0,row=2)
usernameInput.grid(column=1,row=2,columnspan=2)
passwordLabel.grid(column=0,row=3)
passwordInput.grid(column=1,row=3)
passwordButton.grid(column=2,row=3)
addButton.grid(column=1,row=4,columnspan=2)

window.mainloop()