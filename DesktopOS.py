import os
import time as tm
import tkinter as tk

os.system('cls')
tm.sleep(0.2)
print("Initializing..")


from tkinter import *

root = Tk()  # create parent window

def volumeUp():
    '''output message to terminal to tell that the button is working'''
    print("Volume Increase +1")

def volumeDown():
    '''output message to terminal to tell that the button is working'''
    print("Volume Decrease -1")

# use Button and Label widgets to create a simple TV remote
def turnOnSettings():
    '''callback method used for turn_on button'''
    # use a Toplevel widget to display an image in a new window
    window = Toplevel(root)
    window.title("Settings")
    image = PhotoImage(file="plain-3C3C3C.svg")

    original_image = Label(window, image=image)
    original_image.image = image
    original_image.pack()

turn_on = Button(root, text="Settings", command=turnOnSettings)
turn_on.pack()

turn_off = Button(root, text="Exit", command=root.quit)
turn_off.pack()

volume = Label(root, text="VOLUME")
volume.pack()

vol_up = Button(root, text="+", command=volumeUp)
vol_up.pack()

vol_down = Button(root, text="-", command=volumeDown)
vol_down.pack()

window = tk.Tk()

window.attributes('-fullscreen', True)
window.title("MazOS Desktop v0.1.2")

label = tk.Label(window, text="Maz OS Desktop Version")
label.pack()

window.mainloop()






