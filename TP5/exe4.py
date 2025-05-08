

# Étape 1 : Créer le fichier CSV avec des contacts

    # Données à écrire dans le fichier CSV
import csv


contacts = [
        {"Nom": "Ali", "Âge": 30, "Ville": "Agadir"},
        {"Nom": "Ahmed", "Âge": 25, "Ville": "Casa"},
        {"Nom": "Mohammed", "Âge": 35, "Ville": "Rabat"}
    ]

    # Création du fichier CSV avec les colonnes et données
with open('contacts.csv', mode='w', newline= '', encoding='utf-8') as csvfile:
    fieldnames = ['Nom', 'Âge', 'Ville']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Écrire l'en-tête
    writer.writeheader()

    # Écrire les données des contacts
    for contact in contacts:
        writer.writerow(contact)

# Étape 2 : Lire le fichier CSV et afficher les informations dans un format lisible
with open('contacts.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    # Affichage des informations des contacts
    for row in reader:
        print(f"Nom : {row['Nom']}, Âge : {row['Âge']}, Ville : {row['Ville']}")