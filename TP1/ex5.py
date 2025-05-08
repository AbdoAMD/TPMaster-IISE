nombre=int(input("entrez la valeur de n : \n "))
def factorielle(n):
    
    if n == 0 or n == 1: 
        print("le nombre doit etre positive et superieur a 1") 
        return 1
    else:
        return n * factorielle(n - 1)  


resultat = factorielle(nombre)
print(f"La factorielle de {nombre} est {resultat}")