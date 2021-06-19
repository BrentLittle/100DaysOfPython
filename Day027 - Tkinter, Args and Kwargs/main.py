import tkinter

### Creating a window and labels

window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(width = 600, height = 400)

# Label
label = tkinter.Label(text="I am label", font=("Arial", 24, "bold"))
label.pack()
label["text"] = "New Text"

#Button
def btnClicked():
    label["text"] = input.get()

button = tkinter.Button(text="Click Me", command=btnClicked)
button.pack()

#Entry
input = tkinter.Entry(width=30)
input.insert(0, string="Some text to begin with.")
input.pack()

#Text
text = tkinter.Text(height=5, width=30)
text.focus()
text.pack()

# Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
# Called with current scale value.
def scale_used(value):
    print(value)
scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radiobutton
def radio_used():
    print(radio_state.get())
# Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


### Layout Managers
## Pack Place and Grid

# Pack will start at the very top and pack every widget from top to bottom as in a HTML box model

# Place allows you to define a precise position for widgets using X and Y coordinates
    # origin(0,0) is in the top left with X and Y growing horizontally and Veritcally respectively

# Grid
# Rows go along the horizontal and Columns go along the vertical



"""
## Advanced Arguments
## Arguments in a python function can have defualt values but can be modified with values
## passed into the fucntion and it will only change that specific argument and leave the
## others with their default value


### *args: Many Positional Arguments
This allows for unlimited number of positional arguments to be sent to a method

def add(*args):
    for n in args:
        print(n)

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(3,4,5,6))

### **kwards: Arbitrary Number of Keyword Arguments
allows us to process an unlimited number of keyword arguments in a function

def calculate(n, **kwargs):
    print(kwargs)
    for (key,value) in kwargs.items():
        print(key,value)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model= kw.get("model")

myCar = Car(model = "GTR", make="Nissan")
myCar = Car(make="Nissan")
print(myCar.model)
"""



window.mainloop()

    