import random, os, time
import customtkinter as ctk
from modules import hangman as gamef
from pillow import Image

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








# # lista de palavras secretas
# palavras = ["cachorro", "gato", "elefante", "pássaro", "peixe", "leão", "tigre",
#             "girafa", "macaco", "cobra", "lobo", "urso", "rato", "abelha",
#             "borboleta", "aranha", "jacaré", "hipopótamo", "rinoceronte",
#             "esquilo", "zebra", "tartaruga", "camelo", "papagaio", "coruja", 
#             "pinguim", "baleia", "golfinho", "tubarão", "águia", "falcão", 
#             "gavião", "formiga", "escorpião", "lagarto", "coelho", "cisne", 
#             "avestruz", "lontra", "texugo", "ouriço", "leopardo", "hiena", "doninha", 
#             "morcego", "vaca", "porco", "ovelha", "galinha", "pato", "peru", "cavalo", 
#             "cabra", "burro", "coyote", "javali", "veado", "alce", "carpa", "salmão", 
#             "truta", "bagre", "tucunaré", "sardinha", "atum", "caranguejo", "lagosta", 
#             "camarão", "polvo", "lula", "ouriço-do-mar", "estrela-do-mar", "ouriço-do-mar", 
#             "pepino-do-mar", "esponja-do-mar", "medusa", "águia", "urso", "leão", "gato", 
#             "cachorro", "peixe", "tigre", "girafa", "rato", "zebra", "rinoceronte", "leopardo", 
#             "leão-marinho", "lontra", "morcego", "elefante", "avestruz", "papagaio", "golfinho", 
#             "baleia", "orquídea", "rosa", "girassol", "margarida", "lírio", "tulipa", "violeta", 
#             "cravo", "hibisco", "jasmim", "azaléia", "camélia", "hortênsia", "gerânio", "peônia", 
#             "dália", "miosótis", "narciso", "lótus", "flor-de-lis", "begônia", "angélica", "aster", 
#             "mimosa", "verbena", "cipreste", "lírio-do-vale", "tília", "malmequer", "acácia", 
#             "crisântemo", "magnólia", "papoila", "jacinto", "bétula", "sálvia", "lágrima-de-cristo", 
#             "trigo", "milho", "arroz", "cevada", "aveia", "centeio", "sorgo", "millet", "quinoa", 
#             "amendoim", "soja", "feijão", "ervilha", "lentilha", "fava", "grão-de-bico", "trigo-sarraceno", 
#             "linhaça", "chia", "girassol", "gergelim", "nabo", "cenoura", "batata", "beterraba", 
#             "mandioca", "inhame", "batata-doce", "rabano", "agrião", "rucula", "alface", "repolho", 
#             "couve", "espinafre", "acelga", "chicória", "endívia", "almeirão", "mostarda", "abobrinha", 
#             "berinjela", "pimentão", "tomate", "pepino", "abóbora", "quiabo", "milho-verde", 
#             "ervilha-torta", "vagem", "feijão-verde", "couve-flor", "brócolis", "repolho", "nabo", "beterraba", 
#             "cenoura", "batata-doce", "mandioca", "abóbora", "agrião", "rucula", "alface", "espinafre", 
#             "acelga", "chicória", "endívia", "almeirão", "mostarda", "beldroega", "serralha", "urtiga", "urtiga-branca", 
#             "dente-de-leão", "alcaçuz", "arruda", "bálsamo", "bardana", "calêndula", "capuchinha", "carqueja", 
#             "cipó-cabeludo", "copaíba", "equinácea", "espinheira-santa", "guaco", "gengibre", "ginseng", "malva", 
#             "mamona", "poaia", "rosa-brava", "sabugueiro", "salsa", "salsaparrilha", "salgueiro", "sálvia", 
#             "tanchagem", "tuia", "uva-ursi", "vassourinha", "abacaxi", "banana", "maçã", "laranja", "limão", "morango", 
#             "uva", "mamão", "manga", "abacate", "pera", "pêssego", "ameixa", "figo", "kiwi", "melancia", "melão"]


# # início base das variáveis do jogo

# palavra_secreta = palavras[random.randint(0, len(palavras) - 1)] #seleção da palavra secreta escolhida a partir da lista

# letras_acertadas = '' # lista de letras acertadas
# letras_secretas_absolutas = '' # lista de letras corretas sem duplicatas
# numero_de_tentativas = 0 # número de tentativas totais


# # initialize

# print("Bem vindo ao jogo da forca! Vamos começar!")


# while True:

#     # laço para a criação da nova lista sem letras repetidas
#     for letra in palavra_secreta:
#         if letra not in letras_secretas_absolutas:
#             letras_secretas_absolutas += letra

#     # entrada do usuario
#     letra_digitada = input("Digite uma letra: ")
#     numero_de_tentativas += 1

#     os.system("cls")

#     # verificação se o usuário está digitando somente uma letra
#     if len(letra_digitada) > 1:
#         print("Digite apenas uma letra!\n")
#         continue

#     # se a letra digitada estiver na palavra secreta, entrará na lista e letras acertadas
#     if letra_digitada in palavra_secreta:
#         letras_acertadas += letra_digitada


#     # loop percorrendo a palavra secreta, e se a letra percorrida estiver no meio da lista de letras acertadas, imprimirá a letra. E caso não esteja, imprimirá o *
#     for letra_secreta in palavra_secreta:
#         if letra_secreta in letras_acertadas:
#             print(f"{letra_secreta} ", end='')
#         else:
#             print("* ", end='')
#     print('')

#     # estilizando os tracinhos da palavra secreta
#     for letra_secreta in palavra_secreta:
#         print("_ ", end='')
#     print("\n")

#     # se todas as letras acertadas estão na palavra secreta, então temos uma solução


#     if len(letras_acertadas) == len(letras_secretas_absolutas):
#         os.system("cls")

#         print(f"Parabéns, você conseguiu!A palavra secreta é {palavra_secreta}!")
#         print(f"Tentativas: {numero_de_tentativas}")

#         time.sleep(5)

#         palavra_secreta = palavras[random.randint(0, len(palavras) - 1)] #seleção da palavra secreta escolhida a partir da lista

#         letras_acertadas = '' # lista de letras acertadas
#         letras_secretas_absolutas = '' # lista de letras corretas sem duplicatas
#         numero_de_tentativas = 0 # número de tentativas totais

#         os.system("cls")

#         continue
