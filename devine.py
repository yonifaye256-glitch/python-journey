import random
secret = random.randint(1,100)
essaie = 0
tentatives = 0

while essaie != secret:
    essaie = int(input("devine le nombre secret : "))
    tentatives += 1
    if essaie < secret:
        print("trop petit")
    elif essaie > secret:
        print("trop grand")
    else:
        essaie = secret
        print("perfect", tentatives, "essais")
