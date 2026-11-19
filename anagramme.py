mot = "banane"
compteur = {}
for lettre in mot:
    if lettre in compteur:
        compteur[lettre] = compteur[lettre] + 1
    else:
        compteur[lettre] = 1
print(compteur)
        