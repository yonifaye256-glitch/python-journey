secret = 7
essaie = 0

while essaie != secret:
    essaie = int(input("devine le nombre secret : "))
    if essaie < secret:
        print("trop petit")
    elif essaie > secret:
        print("trop grand")
    else:
        essaie = secret
        print("perfect")