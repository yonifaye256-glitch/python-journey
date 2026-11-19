import json
import os
def ajouter(liste, description, montant):
    liste.append({"description": description, "montant": montant})
    
def total(liste):
    somme = 0
    for depense in liste:
        somme = somme + depense["montant"]
    return somme

def sauvegarde(liste):
    with open("depense.json", "w") as f:
        json.dump(liste, f)
        
def charger():
    if os.path.exists("depenses.json"):
        with open ("depenses.json", "r") as f:
            return json.load(f)
        return[]