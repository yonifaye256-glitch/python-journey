import depense
mes_depenses = []
while True:
    print("1. Ajouter une dépense | 2. Afficher le total | q. Quitter")
    choix = input("Ton choix : ")
    if choix == "1":
        description = input("Description de la dépense : ")
        montant = float(input("Montant de la dépense : "))
        depense.ajouter(mes_depenses, description, montant)
    elif choix == "2":
        print("Total des dépenses :", depense.total(mes_depenses))
    elif choix == "q":
        break
    else:
        print("Choix invalide")