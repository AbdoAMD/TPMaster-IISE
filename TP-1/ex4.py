def compte_occurences(liste):
    
    return {mot: liste.count(mot) for mot in set(liste)}

mots = ["ahmed", "ahmed", "said", "samir", "karim", "karim"]
resultat = compte_occurences(mots)
print(resultat) 





