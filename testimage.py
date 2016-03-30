import Tkinter as tk
from PIL import Image, ImageTk
button_flag = True
def click():
    """
    respond to the button click
    """
    global button_flag
    # toggle button colors as a test
    if button_flag:
        button1.config(bg="white")
        button_flag = False
    else:
        button1.config(bg="green")
        button_flag = True
        
def init(self):
    Tk.init (self)
    self.title("periodic Table of the Elements")

    self.topLabel= Label(self, text= "PERIODIC TABLE OF THE ELEMENTS", font=30)
    self.topLabel.grid(row=0,column=0,columnspan=18)
    
root = tk.Tk()
# create a frame and pack it
frame1 = tk.Frame(root)
frame1.pack()
# pick a (small) image file you have in the working directory ...
#column 1
Hydrogen = Image.open('/users/anhdang/Desktop/Hydrogen.gif')
photo1 = ImageTk.PhotoImage(Hydrogen)


button1 = tk.Button(frame1, compound=tk.TOP, width=5, height=20, image=photo1,
    text="optional text", bg='green', command=click)

#Column 16
Oxygen = Image.open('/users/anhdang/Desktop/Oxygen.gif')
photo2 = ImageTk.PhotoImage(Oxygen)


button2 = tk.Button(frame1, compound=tk.TOP, width=5, height=20, image=photo2,
    text="optional text", bg='green', command=click)
#column 14

Carbon = Image.open('/users/anhdang/Desktop/Carbon.gif')
photo3 = ImageTk.PhotoImage(Carbon)


button3 = tk.Button(frame1, compound=tk.TOP, width=5, height=20, image=photo3,
    text="optional text", bg='green', command=click)

Nitrogen = Image.open('/users/anhdang/Desktop/Nitrogen.gif')
photo4 = ImageTk.PhotoImage(Nitrogen)


button4 = tk.Button(frame1, compound=tk.TOP, width=5, height=20, image=photo4,
    text="optional text", bg='green', command=click)
button1.grid( row=1, column=1)
button2.grid(row=1, column=16)
button3.grid(row=1,column=14)
button4.grid(row=1 , column=15)

# save the button's image from garbage collection (needed?)
button1.image = photo1
# start the event loop
root.mainloop()
