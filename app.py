import random, os, time
import customtkinter as ctk
from modules import hangman as gamef

# set theme configutations
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# create the app window
app = ctk.CTk()
app.geometry("800x600")
app.iconbitmap("./hangman.ico")
app.title("Hangman - in python")
app.resizable(False, False)


#------------------------------------- SET THE MAIN WINDOWS WIDGETS -------------------------------------
    

# title
titleLabel = ctk.CTkLabel(master=app, text="Hangman - in Python", fg_color="transparent", text_color="white", font=("Arial", 36, "bold"))
titleLabel.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

# how to play
howToPlayLabel = ctk.CTkLabel(master=app, text="How To Play", fg_color="transparent", text_color="white", font=("Arial", 20, "bold"))
howToPlayLabel.place(relx = 0.1, rely=0.25, anchor=ctk.CENTER)

# description text
description_text = """
Hangman is a classic word-guessing game. Here are the basic rules:

    - One player thinks of a word or phrase, and others try to guess it.
    - The word is represented by dashes, one for each letter.
    - Players guess one letter at a time.
    - If the guessed letter is in the word, it is revealed.
    - If the guessed letter is not in the word, it counts as a wrong guess.
    - Players have a limited number of wrong guesses (usually 6) before losing.
    - Win by guessing the entire word before using all wrong guesses.
"""

# decription implementation
htpDescriptionLabel = ctk.CTkLabel(master=app, text=description_text, fg_color="transparent", text_color="gray", font=("Arial", 14, "bold"), justify="left", anchor=ctk.CENTER, wraplength=750 )
htpDescriptionLabel.place(relx = 0.4, rely=0.43, anchor=ctk.CENTER)


letsPlayLabel = ctk.CTkLabel(master=app, text="Let's Play?", fg_color="transparent", text_color="white", font=("Arial", 20, "bold"))
letsPlayLabel.place(relx = 0.1, rely = 0.62, anchor=ctk.CENTER)

# start game button
playButton = ctk.CTkButton(master=app,command=lambda: gamef.playGameButton(app), hover=True, text="Play Game", border_color="black", border_width=2, fg_color="darkgreen", text_color="white", font=("Arial",30, "bold"), width=100, height= 75, corner_radius=30)
playButton.place(relx = 0.5, rely = 0.80, anchor=ctk.CENTER)


app.mainloop()
