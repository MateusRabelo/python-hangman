import customtkinter as ctk
import random, os, time
from PIL import Image

# counter of attempts
attempts = 5

# set PIL image
imagePath = "./assets/hangman.png"
image = Image.open(imagePath)

# function to debug
def playGameButton(app):
    global attempts
    attempts = 5

    # cleaning screen
    for widget in app.winfo_children():
        widget.destroy()

    # initialize game
    startGame(app)


# game logical
def startGame(app):

    # attempts count
    global attemptsLabel
    attemptsLabel = ctk.CTkLabel(master=app, text=f"Attempts: {attempts}", fg_color="transparent", text_color="#ffffff", font=("Arial", 20, "bold"))
    attemptsLabel.place(relx = 0.5, rely = 0.05, anchor=ctk.CENTER)

    # applying the image on the screen
    global stickImage
    stickImage = ctk.CTkImage(light_image=image, dark_image=image, size=(300, 300))
    stickImageLabel = ctk.CTkLabel(master=app, image=stickImage, text="")
    stickImageLabel.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

    # secret word in line
    wordLabel = ctk.CTkLabel(master=app,text="_ _ _ _ _ _", fg_color="transparent", text_color="#ffffff", font=("Arial", 40, "bold"))
    wordLabel.place(relx = 0.5, rely = 0.72, anchor=ctk.CENTER)

   # word entry
    validation = app.register(validateInput)  # register function to validation
    userEntry = ctk.CTkEntry(master=app, placeholder_text="Digite uma letra", validate="key", validatecommand=(validation, "%P"))
    userEntry.place(relx=0.5, rely=0.88, anchor=ctk.CENTER)

    # input submit
    entrySubmitButton = ctk.CTkButton(master=app, command=submitButtonClicked)
    entrySubmitButton.place(relx = 0.5, rely = 0.95, anchor=ctk.CENTER)


# to validate just a letter
def validateInput(new_value):
    # Permitir apenas uma letra
    if len(new_value) > 1 or not new_value.isalpha():
        return False
    return True


def submitButtonClicked():
    # importing teh global variables
    global attempts, imagePath, image
    
    # counting attempts
    if attempts > 0:
        attempts -= 1
        print(f"Tentativas restantes: {attempts}")
        attemptsLabel.configure(text=f"Attempts: {attempts}")


    # image selectors
    if attempts == 4:
        imagePath = "./assets/hangman-no-left-leg.png"
        image = Image.open(imagePath)
        stickImage.configure(light_image=image, dark_image=image)

    if attempts == 3:
        imagePath = "./assets/hangman-no-legs.png"
        image = Image.open(imagePath)
        stickImage.configure(light_image=image, dark_image=image)

    if attempts == 2:
        imagePath = "./assets/hangman-no-left-arm.png"
        image = Image.open(imagePath)
        stickImage.configure(light_image=image, dark_image=image)

    if attempts == 1:
        imagePath = "./assets/hangman-no-arms.png"
        image = Image.open(imagePath)
        stickImage.configure(light_image=image, dark_image=image)

    if attempts == 0:
        imagePath = "./assets/hangman-death.png"
        image = Image.open(imagePath)
        stickImage.configure(light_image=image, dark_image=image)

    
    

    





# to undestand the validations code
# def as_validate_input(action, index, new_value, old_value, char, validation_type, trigger_type, widget_name):
#     print(f"Action: {action}, Index: {index}, New Value: {new_value}, Old Value: {old_value}, Char: {char}, Validation Type: {validation_type}, Trigger Type: {trigger_type}, Widget Name: {widget_name}")

# validation codes
# validatecommand=(vcmd, "%d", "%i", "%P", "%s", "%S", "%v", "%V", "%W")

