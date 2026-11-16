nom = "Yoni"
age = 24
taille = 1.75
est_etudiant = True

print(nom, type(nom))
print(age, type(age))
print(taille, type(taille))
print(est_etudiant, type(est_etudiant))

print(age + 5)
print(taille * 2)

anee_de_naissance = int(input("quel est votre annee de naissance? "))
age = 2026 - anee_de_naissance
print("mon annee de naissance est", anee_de_naissance)
print("j'ai", age, "ans")