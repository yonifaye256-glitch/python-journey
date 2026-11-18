import calcul
a = float (input("entre un nombre"))
b = float(input("entre un deuxieme"))
op = input("operation (+, -, *, /): ")

if op == "+":
    resultat = calcul.addition(a,b)
elif op == "-":
    resultat = calcul.soustraction(a,b)
elif op =="*":
    resultat = calcul.multiplication(a,b)
    
elif op == "/":
    resultat = calcul.division(a,b)
    
else :
    resultat = None
    print("Resultat :" ,resultat)