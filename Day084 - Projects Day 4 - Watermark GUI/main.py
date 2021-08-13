import os
import tkinter as tk
from tkinter import Label, Button, Entry
from tkinter.filedialog import askopenfilename
from PIL import Image


BACKGROUND_COLOR = "#B1DDC6"
BUTTON_BACKGROUND = "#A1CDB6"

class image:
    def __init__(self):
        self.path = ""

imageToWatermark = image()
watermarkImage = image()

def browsefunc(label, imgObject):
    filename = askopenfilename(filetypes = (("jpeg files","*.jpeg"), ("jpg files","*.jpg"), ("png files","*.png"),
                                         ("All files","*.*")))
    imgObject.path = filename
    label["text"] = filename.split("/")[-1]

def processImg(imageToMark, watermark):
    imgtoWater = Image.open(imageToMark.path)
    watermrk = Image.open(watermark.path)

    resizedWatermrk = watermrk.resize((imgtoWater.size[0], imgtoWater.size[1]))

    imgtoWater.paste(resizedWatermrk, (0,0), mask = resizedWatermrk)
    imgtoWater.save(f"{os.path.dirname(os.path.realpath(__file__))}/WatermarkedImage.jpeg")
    watermarkedFilePathLabel["text"] = f"File Successfully saved at:\n {os.path.dirname(os.path.realpath(__file__))}/WatermarkedImage.jpeg"


# DEFINE GUI WINDOW
window = tk.Tk()
window.geometry('1100x375')
window.title("Typing Speed Test")
window.configure(bg = 'black', padx = 100)


# TITLE
title_label = Label(text = 'ADD A WATERMARK', font = ("Arial", 55, 'bold'), pady = 25, bg = 'black', fg = 'gold')
title_label.grid(row = 0, column = 1)


# INFORMATION LABELS
imgFilePathLabel = Label(font = ("Arial",14,'bold'), bg = 'black', fg = "white")
imgFilePathLabel.grid(row = 2, column = 0)
watermarkFilePathLabel  = Label(font = ("Arial",14,'bold'), bg = 'black', fg = "white")
watermarkFilePathLabel.grid(row = 2, column = 2)
watermarkedFilePathLabel = Label(font = ("Arial",14,'bold'), bg = 'black', fg = "white", wraplength=300)
watermarkedFilePathLabel.grid(row = 3, column = 1, pady=25)


# BUTTONS
selectImgBtn = Button(text = 'SELECT IMAGE',font = ("Arial", 16, 'bold'), command = lambda: browsefunc(imgFilePathLabel, imageToWatermark))
selectImgBtn.grid(row = 1, column = 0, pady = 25)
selectWatermarkBtn = Button(text = 'SELECT WATERMARK', font = ("Arial", 16, 'bold'), command = lambda: browsefunc(watermarkFilePathLabel, watermarkImage))
selectWatermarkBtn.grid(row = 1, column = 2,  pady = 25)
generateResultBtn = Button(text = 'GENERATE RESULT',font = ("Arial", 16, 'bold'), command = lambda: processImg(watermark = watermarkImage, imageToMark = imageToWatermark))
generateResultBtn.grid(row = 2, column = 1, pady = 5)

window.mainloop()
