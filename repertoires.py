import json
import os
if os.path.exists("contact.json"):
    with open("contact.json","r")as f:
        contacts = json.load(f)
else:
    contacts = {}
while True:
        print("1. Ajouter | 2. Chercher | 3. Afficher | q. Quitter")
        choix = input("Ton choix : ")
        if choix == "1":
            nom = input("Nom:")
            numero = input("Numero :")
            contacts[nom] = numero
        elif choix == "2":
            recherche = input("Quel contact cherches tu ?")
            if recherche in contacts:
                print("Numero :", contacts[recherche])
            else:
                print("Contact introuvable")
        elif choix == "3":
            for nom, numero in contacts.items():
                print(nom, ":", numero)
        elif choix == "q":
            with open("contact.json","w") as f:
                json.dump(contacts, f)
                break
        else:
            print("choix invalide")