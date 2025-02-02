def get_positive_integer():
    while True:
        try:
            number = int(input("Veuillez saisir un entier positif : "))
            if number > 0:
                return number
            print("L'entier doit être positif.")
        except ValueError:
            print("Ce n'est pas un entier valide.")

# Exemple d'appel de la fonction
positive_number = get_positive_integer()
print(f"Vous avez saisi l'entier positif : {positive_number}")
