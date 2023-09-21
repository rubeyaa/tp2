#créé par Adam Rubeya
#créé en 2023
#ce code va vous faire deviner un nombre

from random import*
def limite():
    superieur = int(input("Quel est le nombre maximum possible à deviner dans la nouvelle partie?"))
    inferieur= int(input("Quel est le nombre minimum possible a deviner dans la nouvelle partie?"))
    print("J'ai choisi un nombre entre %s et %d. Devinez ce dernier."%(superieur,inferieur))
    reee = randint(superieur,inferieur)
    return reee
variable = limite()
nb_essai = 1
tentative = 0
loop = 0


while loop == 0:
    tentative = int(input("votre essai:"))

    if tentative == variable:
        print("bravo! vous avez eu la bonne réponse en %d nb_essai" %(nb_essai))
        quit()

    else:
        print("Mauvaise réponse, recommencez.")
        nb_essai += 1
        if tentative > variable:
            print("Votre réponse est trop haute.")
        elif tentative < variable:
             print("Votre réponse est trop basse.")
#indique si vous avez eu la bonne réponse
limite()