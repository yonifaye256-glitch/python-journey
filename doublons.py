## O(n^2) lente

def a_doublons(liste):
    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):
            if liste[i]== liste[j]:
                return True
    return False

## O(n) rapide
print(a_doublons([1, 2, 3, 1]))
