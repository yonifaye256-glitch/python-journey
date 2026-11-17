def est_pair(n):
    if n % 2 == 0:
        return True
    else: 
        return False
print(est_pair(6))


def air_rectangulaire(longueur, largeur):
    return longueur * largeur
print(air_rectangulaire(2,2))


def fcfa_vvers_euro(montant):
    euro = montant / 655.957
    return euro
print(fcfa_vvers_euro(23))
    
def euro_vers_fcfa(montant):
    fcfa = montant * 655.957
    return fcfa
print(euro_vers_fcfa(1000))


