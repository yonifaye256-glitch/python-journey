import json
contacts=["Awa :" "770000000", "Moussa :", "781111111" ]
###  Ecrire dans un fichier
with open("contacts.json", "w", encoding= "utf-8") as f:
    json.dump(contacts, f, ensure_ascii="False")
    
### Lire le fichier 
with open("contacts.json" ,"r", encoding="uft-8")as f:
    charges = json.load(f)
    
print(charges)
    
