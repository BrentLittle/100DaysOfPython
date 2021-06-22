import tkinter as tk
from tkinter import messagebox
import random
import json





# ---------------------------- FIND PASSWORD ------------------------------- #
def findPassword():
    websiteName = websiteInput.get()

    try:
        with open('data.json', 'r') as file:  
            # Read old Data
            data = json.load(file)
    
    except FileNotFoundError:  
        messagebox.showinfo(title="File Not Found", message = f"There are no saved Files, Please add a password")        
    
    else:        
        if websiteName in data:  
            email = data[websiteName]["email"]
            password = data[websiteName]["password"]
            messagebox.showinfo(title=websiteName, message = f"\nEmail: {email} \nPassword: {password}")
        
        else:
            messagebox.showinfo(title="Error", message = f"No details found for {websiteName}")
           




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

    newData = {
        websiteName:{
            "email": username,
            "password":password,
        }
    }

    if len(username) == 0 or len(password) == 0 or len(websiteName) == 0:
        
        messagebox.showinfo(title="Oops", message="Please fill out all fields")
        return
        
    else:
        try:
            with open('data.json', 'r') as file:  
                # Read old Data
                data = json.load(file)
        
        except FileNotFoundError:  
            with open('data.json', 'w') as file:  
                json.dump(newData, file, indent=4)   
            
        else:
            # Update the Data with the new addition
            data.update(newData)
            
            with open('data.json', 'w') as file:  
                json.dump(data, file, indent=4)

        finally:  
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
websiteInput    = tk.Entry(width=21)
usernameLabel   = tk.Label(text="Email/Username:")
usernameInput   = tk.Entry(width=36)
passwordLabel   = tk.Label(text="Password:")
passwordInput   = tk.Entry(width=21)
passwordButton  = tk.Button(text="Generate Password", command=generatePassword)
addButton       = tk.Button(text="Add", width=36, command=savePassword)
searchButton    = tk.Button(text="Search", command=findPassword)

usernameInput.insert(0,"BrentLittlefield@email.com")

websiteLabel.grid(column=0,row=1)
websiteInput.grid(column=1,row=1)
usernameLabel.grid(column=0,row=2)
usernameInput.grid(column=1,row=2,columnspan=2)
passwordLabel.grid(column=0,row=3)
passwordInput.grid(column=1,row=3)
passwordButton.grid(column=2,row=3)
addButton.grid(column=1,row=4,columnspan=2)
searchButton.grid(column=2,row=1)

window.mainloop()