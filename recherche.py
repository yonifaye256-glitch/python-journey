contacts={}
while True:
    recherche = input("quel est votre contact ?")
    if recherche in contacts:
        print("Numero :", contacts[recherche])
    else:
        print("contact non trouvé")
        
    nom =input("nom(q pour sortir):")
    if nom == "q":
        break
    numero =input("numero: ")
    contacts[nom] = numero
    for nom, numero in contacts.items:
        print (nom, numero)