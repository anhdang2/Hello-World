from Tkinter import *
from PIL import Image
import pyautogui, sys

def clickrec

def callback(event):
    canvas = event.widget
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    print canvas.find_closest(x, y)
    
root=Tk()


root.title("PeriodicTableOfElements")
root.geometry("1600x768")

photo= PhotoImage(file="periodictable1.gif")
label=Label(root, image=photo)
label.pack()



root.mainloop()
