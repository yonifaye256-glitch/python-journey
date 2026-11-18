try:
    age = int(input("Ton age: "))
    print(" Dans 10 ans tu aura :", age)
except ValueError:
    print(" Ce n'est pas un nombre")