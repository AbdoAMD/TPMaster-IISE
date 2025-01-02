# Ouverture du fichier en mode lecture
with open('exemple.txt') as file:
    # Lire toutes les lignes du fichier
    lines = file.readlines()

    # Affichage de chaque ligne avec son numéro
    for i, line in enumerate(lines, 1):
        print(f"Ligne {i}: {line.strip()}")
