carnet ={}
nom = (input("entrez votre nom"))
numero = (input("etrez votre numero"))
carnet [nom]= numero
print(carnet)

contact={}
while True:
    nom = input("nom (q pour quitter):")
    if nom == "q":
        break
    numero = input("numero:")
    contact [nom] = numero
    
for nom, numero in contact.items():
    print(nom, ":", numero)