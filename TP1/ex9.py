text=input("entrez une phrase: \n ")
def analyse_texte(texte):
    mots = texte.split()
    
    nb_mots = len(mots)
    
    nb_caracteres = sum(len(mot) for mot in mots)
    
    return {"nombre_mots": nb_mots,"nombre_caracteres": nb_caracteres}

resultat = analyse_texte(text)
print(resultat)