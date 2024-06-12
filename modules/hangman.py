import customtkinter as ctk
import random, os, time

# counter of attempts
attempts = 5

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

    # secret word in line
    wordLabel = ctk.CTkLabel(master=app,text="_ _ _ _ _ _", fg_color="transparent", text_color="#ffffff", font=("Arial", 40, "bold"))
    wordLabel.place(relx = 0.5, rely = 0.5, anchor=ctk.CENTER)

    # attempts count
    global attemptsLabel
    attemptsLabel = ctk.CTkLabel(master=app, text=f"Attempts: {attempts}", fg_color="transparent", text_color="#ffffff", font=("Arial", 20, "bold"))
    attemptsLabel.place(relx = 0.5, rely = 0.3, anchor=ctk.CENTER)

   # Configurar entrada de texto para aceitar apenas uma letra
    validation = app.register(validateInput)  # Registrar função de validação
    userEntry = ctk.CTkEntry(master=app, placeholder_text="Digite uma letra", validate="key", validatecommand=(validation, "%P"))
    userEntry.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

    # input submit
    entrySubmitButton = ctk.CTkButton(master=app, command=submitButtonClicked)
    entrySubmitButton.place(relx = 0.5, rely = 0.6, anchor=ctk.CENTER)


# to validate just a letter
def validateInput(new_value):
    # Permitir apenas uma letra
    if len(new_value) > 1 or not new_value.isalpha():
        return False
    return True


def submitButtonClicked():
    global attempts
    
    if attempts > 0:
        attempts -= 1
        print(f"Tentativas restantes: {attempts}")
        attemptsLabel.configure(text=f"Attempts: {attempts}")

    # else:
        # EndGame();





# to undestand the validations code
# def as_validate_input(action, index, new_value, old_value, char, validation_type, trigger_type, widget_name):
#     print(f"Action: {action}, Index: {index}, New Value: {new_value}, Old Value: {old_value}, Char: {char}, Validation Type: {validation_type}, Trigger Type: {trigger_type}, Widget Name: {widget_name}")

# validation codes
# validatecommand=(vcmd, "%d", "%i", "%P", "%s", "%S", "%v", "%V", "%W")

