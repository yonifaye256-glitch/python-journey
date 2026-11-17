notes = [12, 15, 9, 18]
def statistiques(liste):
    moyenne = sum(liste) / len(liste)
    maximum = max(liste)
    minimum = min(liste)
    return moyenne, maximum, minimum
moy, maxi, mini, = statistiques([12, 15, 9, 18])
print ("Moyenne:",moy , "Max :", maxi, "Min:", mini)


notes =[]
for i in range(5):
    note = float(input("entrer 5 nombres"))
    notes.append(note)
    
print(notes)
moy, maxi, mini, = statistiques(notes)
print ("Moyenne:",moy , "Max :", maxi, "Min:", mini)


    
    
