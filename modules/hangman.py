import customtkinter as ctk
import random, os, time
from PIL import Image

# counter of attempts
attempts = 5

# set PIL image
stickImagePath = "./assets/stick/hangman.png"
stickImageOpen = Image.open(stickImagePath)

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
    stickImage = ctk.CTkImage(light_image=stickImageOpen, dark_image=stickImageOpen, size=(400, 350))
    stickImageLabel = ctk.CTkLabel(master=app, image=stickImage, text="")
    stickImageLabel.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

    # secret word in line
    wordLabel = ctk.CTkLabel(master=app,text="_ _ _ _ _ _", fg_color="transparent", text_color="#ffffff", font=("Arial", 40, "bold"))
    wordLabel.place(relx = 0.5, rely = 0.72, anchor=ctk.CENTER)

   # validation to app.register
    vcmd = (app.register(validateInput), '%P')  # register function to validation

    # user word entry
    global userEntry
    user_input_var = ctk.StringVar()
    userEntry = ctk.CTkEntry(master=app, placeholder_text="Digite uma letra", textvariable=user_input_var, validate="key", validatecommand=vcmd, width=30, height=20, justify="center")
    userEntry.place(relx=0.5, rely=0.85, anchor=ctk.CENTER)

    # input submit
    entrySubmitButton = ctk.CTkButton(master=app, command=lambda: submitButtonClicked(app), text="Submit", text_color="white", width=50, height=20)
    entrySubmitButton.place(relx = 0.5, rely = 0.922, anchor=ctk.CENTER)


# to validate just a letter
def validateInput(P):
    # Verifica se a entrada é vazia ou contém apenas uma letra
    return P == "" or (len(P) == 1 and P.isalpha())


def submitButtonClicked(app):
    # importing teh global variables
    global attempts, stickImagePath, stickImageOpen

    userInput = userEntry.get()
    print(f'Input do usuário: {userInput}')

    
    # counting attempts
    if attempts > 0:
        attempts -= 1
        print(f"Tentativas restantes: {attempts}")
        attemptsLabel.configure(text=f"Attempts: {attempts}")

    try:
        # Usar after para garantir que a interface gráfica está atualizada
        app.after(100, lambda: userEntry.delete(0, 'end'))
    except Exception as e:
        print(f"Erro ao tentar limpar a entrada: {e}")
    
    # image selectors
    if attempts == 4:
        stickImagePath = "./assets/stick/hangman-no-left-leg.png"
        stickImageOpen = Image.open(stickImagePath)
        stickImage.configure(light_image=stickImageOpen, dark_image=stickImageOpen)

    if attempts == 3:
        stickImagePath = "./assets/stick/hangman-no-legs.png"
        stickImageOpen = Image.open(stickImagePath)
        stickImage.configure(light_image=stickImageOpen, dark_image=stickImageOpen)

    if attempts == 2:
        stickImagePath = "./assets/stick/hangman-no-left-arm.png"
        stickImageOpen = Image.open(stickImagePath)
        stickImage.configure(light_image=stickImageOpen, dark_image=stickImageOpen)

    if attempts == 1:
        stickImagePath = "./assets/stick/hangman-no-arms.png"
        stickImageOpen = Image.open(stickImagePath)
        stickImage.configure(light_image=stickImageOpen, dark_image=stickImageOpen)

    if attempts == 0:
        stickImagePath = "./assets/stick/hangman-death.png"
        stickImageOpen = Image.open(stickImagePath)
        stickImage.configure(light_image=stickImageOpen, dark_image=stickImageOpen)

    
    

    





# to undestand the validations code
# def as_validate_input(action, index, new_value, old_value, char, validation_type, trigger_type, widget_name):
#     print(f"Action: {action}, Index: {index}, New Value: {new_value}, Old Value: {old_value}, Char: {char}, Validation Type: {validation_type}, Trigger Type: {trigger_type}, Widget Name: {widget_name}")

# validation codes
# validatecommand=(vcmd, "%d", "%i", "%P", "%s", "%S", "%v", "%V", "%W")

