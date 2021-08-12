import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image


BACKGROUND_COLOR = "#B1DDC6"
BUTTON_BACKGROUND = "#A1CDB6"

class image:
    def __init__(self):
        self.path = ""

imageToWatermark = image()
watermarkImage = image()

window = tk.Tk()
window.title("Watermark Adder")
window.config(padx = 25, pady = 25, bg = BACKGROUND_COLOR) 

imgFilePathLabel = tk.Label(window,font = 40, width = 0, bg = BACKGROUND_COLOR)
watermarkFilePathLabel = tk.Label(window,font = 40,width = 0, bg = BACKGROUND_COLOR)
watermarkedFilePathLabel = tk.Label(window,font = 40,width = 0, bg = BACKGROUND_COLOR)


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


getImgFilePathBtn = tk.Button(window, highlightbackground = BUTTON_BACKGROUND, text = "Select Image File", 
                            font = 40, command = lambda: browsefunc(imgFilePathLabel, imageToWatermark))
getWatermarkFilePathBtn = tk.Button(window, highlightbackground = BUTTON_BACKGROUND, text = "Select watermark File", 
                                  font = 40, command = lambda: browsefunc(watermarkFilePathLabel, watermarkImage))
getWatermarkImgBtn = tk.Button(window, highlightbackground = BUTTON_BACKGROUND, text = "Generate Watermarked Image", 
                            font = 40, command = lambda: processImg(watermark = watermarkImage, imageToMark = imageToWatermark))

getImgFilePathBtn.grid(row = 1,column = 1)
imgFilePathLabel.grid(row = 2,column = 1)
getWatermarkFilePathBtn.grid(row = 3,column = 1)
watermarkFilePathLabel.grid(row = 4,column = 1)
getWatermarkImgBtn.grid(row = 5,column = 1)
watermarkedFilePathLabel.grid(row = 6,column = 1)

window.mainloop()
