from tkinter import *
import random
from time import sleep, time


def roll():
    die = random.randrange(1, 7)
    faces = list(dice.values())
    random.shuffle(faces)

    for face in faces:
        rolled.configure(text=face, fg="red")
        rolled.pack()
        root.update()

        sleep(0.13)

    rolled.configure(text=f"{dice[die]}", fg="green")
    rolled.pack()
    root.update()


random.seed(time())

dice = {
    1: "\u2680",
    2: "\u2681",
    3: "\u2682",
    4: "\u2683",
    5: "\u2684",
    6: "\u2685"
}

root = Tk()
root.title("🎲 Dice Simulator 🎲")
root.configure(background="black")

root.geometry("300x200+500+200")
root.resizable(False, False)

roll_button = Button(
    root,
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

rolled = Label(root, font=("times", 120), bg="black")
rolled.configure(text=f"{dice[random.randrange(1, 7)]}", fg="green")
rolled.pack()

root.mainloop()
