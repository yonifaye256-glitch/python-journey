import json
contact={ "Amy": "770000001"}
with open("contact.json", "w") as f:
    json.dump(contact, f)
    
with open("contact.json", "r")as f:
    charges = json.load(f)
print(charges)