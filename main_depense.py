import depense
mes_depenses = depense.charger()
while True:
    print("1. Ajouter une dépense | 2. Afficher le total | q. Quitter |4. Supprimer ")
    choix = input("Ton choix : ")
    if choix == "1":
        description = input("Description de la dépense : ")
        try:
            montant = float(input("Montant de la dépense : "))
            depense.ajouter(mes_depenses, description, montant)
        except ValueError:
            print("Entrer un nombre valide")
    elif choix == "2":
        for i, depense in enumerate(mes_depenses, 1):
            print(i, ".", depense["desciption"], ":", depense["montant"])
    elif choix == "q":
        depense.sauvegarde(mes_depenses)
        break
    elif choix == "4":
        try:
            numero = int(input("Numero a supprimer :"))
            if depense.supprimer(mes_depenses, numero):
                print("supprimer")
            else:
                print("Numero introuvable")
        except ValueError:
            print("entrer un nombre valide")
    else:
        print("Choix invalide")