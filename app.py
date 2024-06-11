import random
import os
import time
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x240")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()





# lista de palavras secretas
palavras = ["cachorro", "gato", "elefante", "pássaro", "peixe", "leão", "tigre",
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


# início base das variáveis do jogo

palavra_secreta = palavras[random.randint(0, len(palavras) - 1)] #seleção da palavra secreta escolhida a partir da lista

letras_acertadas = '' # lista de letras acertadas
letras_secretas_absolutas = '' # lista de letras corretas sem duplicatas
numero_de_tentativas = 0 # número de tentativas totais


# initialize

print("Bem vindo ao jogo da forca! Vamos começar!")


while True:

    # laço para a criação da nova lista sem letras repetidas
    for letra in palavra_secreta:
        if letra not in letras_secretas_absolutas:
            letras_secretas_absolutas += letra

    # entrada do usuario
    letra_digitada = input("Digite uma letra: ")
    numero_de_tentativas += 1

    os.system("cls")

    # verificação se o usuário está digitando somente uma letra
    if len(letra_digitada) > 1:
        print("Digite apenas uma letra!\n")
        continue

    # se a letra digitada estiver na palavra secreta, entrará na lista e letras acertadas
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada


    # loop percorrendo a palavra secreta, e se a letra percorrida estiver no meio da lista de letras acertadas, imprimirá a letra. E caso não esteja, imprimirá o *
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            print(f"{letra_secreta} ", end='')
        else:
            print("* ", end='')
    print('')

    # estilizando os tracinhos da palavra secreta
    for letra_secreta in palavra_secreta:
        print("_ ", end='')
    print("\n")

    # se todas as letras acertadas estão na palavra secreta, então temos uma solução


    if len(letras_acertadas) == len(letras_secretas_absolutas):
        os.system("cls")

        print(f"Parabéns, você conseguiu!A palavra secreta é {palavra_secreta}!")
        print(f"Tentativas: {numero_de_tentativas}")

        time.sleep(5)

        palavra_secreta = palavras[random.randint(0, len(palavras) - 1)] #seleção da palavra secreta escolhida a partir da lista

        letras_acertadas = '' # lista de letras acertadas
        letras_secretas_absolutas = '' # lista de letras corretas sem duplicatas
        numero_de_tentativas = 0 # número de tentativas totais

        os.system("cls")

        continue