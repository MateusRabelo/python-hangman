import customtkinter as ctk
import random
from PIL import Image

# list of secret words
words = ["cachorro", "gato", "elefante", "pássaro", "peixe", "leão", "tigre",
            "girafa", "macaco", "cobra", "lobo", "urso", "rato", "abelha",
            "borboleta", "aranha", "jacaré", "hipopótamo", "rinoceronte",
            "esquilo", "zebra", "tartaruga", "camelo", "papagaio", "coruja", 
            "pinguim", "baleia", "golfinho", "tubarão", "águia", "falcão", 
            "gavião", "formiga", "escorpião", "lagarto", "coelho", "cisne", 
            "avestruz", "lontra", "texugo", "ouriço", "leopardo", "hiena", "doninha", 
            "morcego", "vaca", "porco", "ovelha", "galinha", "pato", "peru", "cavalo", 
            "cabra", "burro", "coyote", "javali", "veado", "alce", "carpa", "salmão", 
            "truta", "bagre", "tucunaré", "sardinha", "atum", "caranguejo", "lagosta", 
            "camarão", "polvo", "lula", "ouriço-do-mar", "estrela-do-mar", "ouriço-do-mar", 
            "pepino-do-mar", "esponja-do-mar", "medusa", "águia", "urso", "leão", "gato", 
            "cachorro", "peixe", "tigre", "girafa", "rato", "zebra", "rinoceronte", "leopardo", 
            "leão-marinho", "lontra", "morcego", "elefante", "avestruz", "papagaio", "golfinho", 
            "baleia", "orquídea", "rosa", "girassol", "margarida", "lírio", "tulipa", "violeta", 
            "cravo", "hibisco", "jasmim", "azaléia", "camélia", "hortênsia", "gerânio", "peônia", 
            "dália", "miosótis", "narciso", "lótus", "flor-de-lis", "begônia", "angélica", "aster", 
            "mimosa", "verbena", "cipreste", "lírio-do-vale", "tília", "malmequer", "acácia", 
            "crisântemo", "magnólia", "papoila", "jacinto", "bétula", "sálvia", "lágrima-de-cristo", 
            "trigo", "milho", "arroz", "cevada", "aveia", "centeio", "sorgo", "millet", "quinoa", 
            "amendoim", "soja", "feijão", "ervilha", "lentilha", "fava", "grão-de-bico", "trigo-sarraceno", 
            "linhaça", "chia", "girassol", "gergelim", "nabo", "cenoura", "batata", "beterraba", 
            "mandioca", "inhame", "batata-doce", "rabano", "agrião", "rucula", "alface", "repolho", 
            "couve", "espinafre", "acelga", "chicória", "endívia", "almeirão", "mostarda", "abobrinha", 
            "berinjela", "pimentão", "tomate", "pepino", "abóbora", "quiabo", "milho-verde", 
            "ervilha-torta", "vagem", "feijão-verde", "couve-flor", "brócolis", "repolho", "nabo", "beterraba", 
            "cenoura", "batata-doce", "mandioca", "abóbora", "agrião", "rucula", "alface", "espinafre", 
            "acelga", "chicória", "endívia", "almeirão", "mostarda", "beldroega", "serralha", "urtiga", "urtiga-branca", 
            "dente-de-leão", "alcaçuz", "arruda", "bálsamo", "bardana", "calêndula", "capuchinha", "carqueja", 
            "cipó-cabeludo", "copaíba", "equinácea", "espinheira-santa", "guaco", "gengibre", "ginseng", "malva", 
            "mamona", "poaia", "rosa-brava", "sabugueiro", "salsa", "salsaparrilha", "salgueiro", "sálvia", 
            "tanchagem", "tuia", "uva-ursi", "vassourinha", "abacaxi", "banana", "maçã", "laranja", "limão", "morango", 
            "uva", "mamão", "manga", "abacate", "pera", "pêssego", "ameixa", "figo", "kiwi", "melancia", "melão"]

#------------------------------------- STARTING BASE VARIABLES OF THE GAME -------------------------------------

# Select a random secret word
secret_word = "mao" #random.choice(words)
right_word = set()  # Set of correct letters

# counter of attempts
attempts = 5

# set PIL image
# stickImagePath = "./assets/stick/hangman.png"
stickImageOpen = Image.open("./assets/stick/hangman.png")

# refreshImagePath = "" 
refreshImageOpen = Image.open("./assets/refresh.png")

# nextImagePath = ""
nextImageOpen = Image.open("./assets/go-arrow.png")

# backImagePath = "" 
backImageOpen = Image.open("./assets/back-arrow.png")   

# function to debug
def playGameButton(app):
    
    global attempts
    attempts = 5

    # cleaning screen
    for widget in app.winfo_children():
        widget.destroy()

    # initialize game
    startGame(app)



# initialize game logic
def startGame(app):

    global attemptsLabel, wordLabel, userEntry, stickImage, right_word, secret_word

    # attempts count
    attemptsLabel = ctk.CTkLabel(master=app, text=f"Remaining Attempts: {attempts}", fg_color="transparent", text_color="#ffffff", font=("Arial", 20, "bold"))
    attemptsLabel.place(relx = 0.5, rely = 0.05, anchor=ctk.CENTER)

    # applying the image on the screen
    stickImage = ctk.CTkImage(light_image=stickImageOpen, dark_image=stickImageOpen, size=(400, 350))
    stickImageLabel = ctk.CTkLabel(master=app, image=stickImage, text="")
    stickImageLabel.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

    # display the secret word as underscores
    display_word = ' '.join(['_' for _ in secret_word])
    wordLabel = ctk.CTkLabel(master=app, text=display_word, fg_color="transparent", text_color="#ffffff", font=("Arial", 40, "bold"))
    wordLabel.place(relx=0.5,rely=0.72, anchor=ctk.CENTER)

   # validation to app.register
    vcmd = (app.register(validateInput), '%P')  # register function to validation

    # user word entry
    user_input_var = ctk.StringVar()
    userEntry = ctk.CTkEntry(master=app, placeholder_text="Digite uma letra", textvariable=user_input_var, validate="key", validatecommand=vcmd, width=30, height=20, justify="center")
    userEntry.place(relx=0.5, rely=0.85, anchor=ctk.CENTER)

    # input submit
    submitButtonImage = ctk.CTkImage(light_image=nextImageOpen, dark_image=nextImageOpen, size=(30,30))
    entrySubmitButton = ctk.CTkButton(master=app, command=lambda: submitButtonClicked(app), image=submitButtonImage, text="Submit", text_color="white", width=50, height=20)
    entrySubmitButton.place(relx = 0.5, rely = 0.922, anchor=ctk.CENTER)


# response to submit and update all all variables
def submitButtonClicked(app):

    # importing teh global variables
    global attempts, stickImageOpen, right_word, secret_word

    guessed_letter = userEntry.get().lower()
    print(f'Input do usuário: {guessed_letter}')

    # Check if guessed letter is in the secret word
    if guessed_letter in secret_word:
        right_word.add(guessed_letter)

    # update displayed word
    updateWordLabel()
    
    # counting attempts
    if attempts > 0:
        attempts -= 1
        print(f"Tentativas restantes: {attempts}")
        attemptsLabel.configure(text=f"Remaining Attempts: {attempts}")

    try:
        # Usar after para garantir que a interface gráfica está atualizada
        app.after(100, lambda: userEntry.delete(0, 'end'))
    except Exception as e:
        print(f"Erro ao tentar limpar a entrada: {e}")
    
    # image selectors
    if attempts == 4:
        # stickImagePath = "./assets/stick/hangman-no-left-leg.png"
        stickImageOpen = Image.open("./assets/stick/hangman-no-left-leg.png")
        # stickImage.configure(light_image=stickImageOpen, dark_image=stickImageOpen)

    if attempts == 3:
        # stickImagePath = "./assets/stick/hangman-no-legs.png"
        stickImageOpen = Image.open("./assets/stick/hangman-no-legs.png")
        # stickImage.configure(light_image=stickImageOpen, dark_image=stickImageOpen)

    if attempts == 2:
        # stickImagePath = "./assets/stick/hangman-no-left-arm.png"
        stickImageOpen = Image.open( "./assets/stick/hangman-no-left-arm.png")
        # stickImage.configure(light_image=stickImageOpen, dark_image=stickImageOpen)

    if attempts == 1:
        # stickImagePath = "./assets/stick/hangman-no-arms.png"
        stickImageOpen = Image.open("./assets/stick/hangman-no-arms.png")
        # stickImage.configure(light_image=stickImageOpen, dark_image=stickImageOpen)

    if attempts == 0:
        # stickImagePath = "./assets/stick/hangman-death.png"
        stickImageOpen = Image.open("./assets/stick/hangman-death.png")
        # stickImage.configure(light_image=stickImageOpen, dark_image=stickImageOpen)

    stickImage.configure(light_image=stickImageOpen, dark_image=stickImageOpen)

    testePalavraSecreta = set(secret_word)
    print(f"palavra sercreta: {testePalavraSecreta}\nLetras acertadas: {right_word}")

    # Check if the player has won
    if set(secret_word) == right_word:
        print(f"Parabéns, você conseguiu! A palavra secreta é {secret_word}!")

        wordLabel.configure(text="You Won!")
        
        # (after accept to receive functions with lambda to work)
        app.after(2000, lambda: restartGame(app))  # Wait for 2 seconds before restarting the game
        
    # Check if the player has lost
    elif attempts == 0:
        print("Você perdeu! A palavra secreta era:", secret_word)

        wordLabel.configure(text="You Lose!")

        app.after(2000, lambda: restartGame(app)) 



# to validate just a letter
def validateInput(P):

    # verify if the input is empty or have just a letter
    return P == "" or (len(P) == 1 and P.isalpha())



def updateWordLabel():

    global secret_word, right_word, wordLabel

    display_word = ""
    for letter in secret_word:
        if letter in right_word:
            display_word += f"{letter} "
        else:
            display_word += "_ "
    
    # Update the word label text
    wordLabel.configure(text=display_word.strip())



# function to reset all variables of the game
def restartGame(app):
    global secret_word, right_word, attempts, stickImage, wordLabel, stickImageOpen

    stickImageOpen = Image.open("./assets/stick/hangman.png")
    stickImage.configure(light_image=stickImageOpen, dark_image=stickImageOpen)

    secret_word = random.choice(words)
    
    right_word.clear()

    attempts = 5

    attemptsLabel.configure(text=f"Attempts: {attempts}")

    playGameButton(app) # reset the game interface before the update of word

    updateWordLabel()
