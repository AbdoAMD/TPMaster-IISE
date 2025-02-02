def main():
    # Demander un fichier
    while True:
        try:
            nom_fichier = input("Veuillez saisir le nom du fichier : ")
            with open(nom_fichier, 'r') as fichier:
                print(f"Fichier '{nom_fichier}' ouvert avec succès.")
                print("Contenu du fichier :")
                print(fichier.read())  # Affiche tout le contenu du fichier
                break  # Sort de la boucle si le fichier est ouvert avec succès
        except (FileNotFoundError, PermissionError) as e:
            print(f"Erreur : {e}. Essayez à nouveau.")

    # Demander un entier  
    while True:
        try:
            entier = int(input("Veuillez saisir un entier : "))
            print(f"Vous avez saisi l'entier : {entier}")
            break
        except ValueError:
            print("Erreur : Ce n'est pas un entier valide. Essayez encore.")

if __name__ == "__main__":
    main()

