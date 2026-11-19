import depense
mes_depenses = depense.charger()
while True:
    print("1. Ajouter une dépense | 2. Afficher le total | q. Quitter")
    choix = input("Ton choix : ")
    if choix == "1":
        description = input("Description de la dépense : ")
        try:
            montant = float(input("Montant de la dépense : "))
            depense.ajouter(mes_depenses, description, montant)
        except ValueError:
            print("Entrer un nombre valide")
    elif choix == "2":
        print("Total des dépenses :", depense.total(mes_depenses))
    elif choix == "q":
        depense.sauvegarde(mes_depenses)
        break
    else:
        print("Choix invalide")