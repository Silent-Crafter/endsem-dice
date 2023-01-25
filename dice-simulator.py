from tkinter import *
import random
from time import sleep


# Function to handle the rolling of dice
def roll():
    # List of all faces
    faces = list(dice.values())

    # Shuffles a given list
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
dice = {
    1: "\u2680",
    2: "\u2681",
    3: "\u2682",
    4: "\u2683",
    5: "\u2684",
    6: "\u2685"
}

parent = Tk()
parent.title("🎲 Dice Simulator 🎲")
parent.configure(background="black")

parent.geometry("300x200+500+200")
# Make the window resizable
parent.resizable(False, False)

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

rolled = Label(parent, font=("times", 120), bg="black")
rolled.configure(text=random.choice(dice), fg="green")
rolled.pack()

parent.mainloop()
