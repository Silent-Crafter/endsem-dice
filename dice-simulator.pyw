#!/usr/bin/python3
import random
from time import sleep
from tkinter import Tk, Button, Label


# Function to handle the rolling of dice
def roll():
    # Shuffles the given list
    random.shuffle(faces)

    # Iterate through the faces to simulate a rolling dice
    for face in faces:
        # Change the rolled label and update the parent window to apply the changes
        rolled.configure(text=face, fg="red")
        rolled.pack()
        parent.update()

        # Animation delay
        sleep(0.13)

    # Finally, choose a random die face
    rolled.configure(text=random.choice(faces), fg="green")
    rolled.pack()
    parent.update()


# A dictionary to store dice faces in unicode
faces = [
    "\u2680",
    "\u2681",
    "\u2682",
    "\u2683",
    "\u2684",
    "\u2685"
]

parent = Tk()
parent.title("Dice Simulator")
parent.configure(background="black")

# Dynamically sets the position of the window to center of screen,
# according to the current screen resolution
res_x = parent.winfo_screenwidth()
res_y = parent.winfo_screenheight()
width = 300
height = 200
x = (res_x - width) // 2
y = (res_y - height) // 2

parent.geometry(f"{width}x{height}+{x}+{y}")
# Make the window resizable
#parent.resizable(False, False)

# Create roll button
roll_button = Button(
    parent,
    text="Roll",
    width=10,
    height=2,
    font=48,
    bg="lightgreen",
    fg="blue",
    bd=2,
    highlightcolor="red",
    highlightbackground="red",
    highlightthickness=2,
    command=roll
)
roll_button.pack(padx=10, pady=15)

# Create a label to show dice face
rolled = Label(parent, font=("times", 120), bg="black")
rolled.configure(text=random.choice(faces), fg="green")
rolled.pack()

parent.mainloop()
