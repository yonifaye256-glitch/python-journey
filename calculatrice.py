a = float(input("entrer un premier nombre"))
b = float(input("entrer un deuxieme nombre"))
op = input("Operation(+, -, *, /)")

if op == "+":
    print("Resultat:" ,a+b)
elif op == "=":
    print("Resultat:", a-b)
elif op =="*":
    print("Resultat:", a*b)
elif op =="/":
    if b == 0:
        print("Impossible")
    else:
        print("resultat", a /b)
else:
        print("Operation inconnuée")

