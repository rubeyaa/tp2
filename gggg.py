#créé par Adam Rubeya
#créé en 2023
#ce code va vous faire deviner un nombre

from random import*
playagain = "oui"
nb_essai = 1
tentative = 0
loop = 0
def limite():
    superieur = int(input("Quel est le nombre maximum possible à deviner dans la nouvelle partie?"))
    inferieur= int(input("Quel est le nombre minimum possible a deviner dans la nouvelle partie?"))
    print("J'ai choisi un nombre entre %s et %d. Devinez ce dernier."%(superieur,inferieur))
    reee = randint(inferieur,superieur)
    return reee

while playagain == "oui":
    variable = limite()
    playagain = "oui"
    nb_essai = 1
    tentative = -2
    loop = 0

    # d'autres variables

    while tentative != variable:
        tentative = int(input("votre essai:"))



        if tentative == variable:
            print("bravo! vous avez eu la bonne réponse en %d nb_essai" %(nb_essai))


        else:
            print("Mauvaise réponse, recommencez.")
            nb_essai += 1
            if tentative > variable:
                print("Votre réponse est trop haute.")
            elif tentative < variable:
                 print("Votre réponse est trop basse.")
    #indique si vous avez eu la bonne réponse

    playagain = str(input("Voulez vous rejouer?"))
#le code vous demande si vous voulez rejouer au jeu à l'aide de playagain

