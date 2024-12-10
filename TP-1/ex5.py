nombre=int(input("entrez la valeur de n : \n "))
def factorielle(n):
    
    if n == 0 :  
        return 1
    else:
        return n * factorielle(n - 1)  


resultat = factorielle(nombre)
print(f"La factorielle de {nombre} est {resultat}")