import tkinter
def convertMileToKM():
    miles = int(milesinput.get())
    resultLabel["text"] = str(round(miles * 1.6,2))
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=25,pady=25)

milesinput =    tkinter.Entry(width=10)
milesLabel =    tkinter.Label(text="Miles")
equalToLabel =  tkinter.Label(text="is equal to")
resultLabel =   tkinter.Label(text="0")
kmLabel =       tkinter.Label(text="Km")
calcButton =    tkinter.Button(text="Calculate", command=convertMileToKM)

milesinput.grid(column=1,row=0)
milesLabel.grid(column=2,row=0)
equalToLabel.grid(column=0,row=1)
resultLabel.grid(column=1,row=1)
kmLabel.grid(column=2,row=1)
calcButton.grid(column=1,row=2)


window.mainloop()