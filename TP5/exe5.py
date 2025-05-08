import json

etudiants = {
    "etudiants": [
        {"Nom": "Ali","Age": 23,"Note": 16},
        {"Nom": "Omar","Age": 22,"Note": 18},
        {"Nom": "Oussama","Age": 22,"Note": 17.5}
    ]
}

try:
    with open("TP5/etudiants.json","w") as fichierjson:
        json.dump(etudiants, fichierjson, indent=4) 
    print(f"Le fichier a été créé avec succès et les informations ont été enregistrées.")
except Exception as e:
    print(f"Une erreur est survenue lors de la création du fichier : {e}")

try:
    with open("TP5/etudiants.json","r") as fichierjson:
        donnees = json.load(fichierjson)
except Exception as e:
    print(f"Une erreur est survenue lors de la lecture du fichier : {e}")

for etudiant in donnees["etudiants"]:
    print(f"Nom : {etudiant['Nom']}, Âge : {etudiant['Age']}, Note : {etudiant['Note']}")