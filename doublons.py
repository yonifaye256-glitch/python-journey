## O(n^2) lente

def a_doublons(liste):
    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):
            if liste[i]== liste[j]:
                return True
    return False

## O(n) rapide
print(a_doublons([1, 2, 3, 1]))

def a_doublons_rapide(liste):
    vus = set()
    for nombre in liste:
        if nombre in vus:
            return True
        vus.add(nombre)
        return False


import time
nombres = list(range(5000))
debut = time.time()     # heure de depart rangé dans debut
a_doublons(nombres)     # le travail a mesurer
print("Lente :", time.time() - debut, "secondes")

debut = time.time()
a_doublons_rapide(nombres)
print("Rapide :", time.time() - debut, "second")

