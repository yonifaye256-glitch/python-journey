def ajouter(liste, description, montant):
    liste.append({"description": description, "montant": montant})
    
def total(liste):
    somme = 0
    for depense in liste:
        somme = somme + depense["montant"]
    return somme