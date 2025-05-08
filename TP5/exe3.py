def ajouter_phrases():
    phrase = input("Entrez une phrase: ")
    with open("phrases.txt", "a") as file:  # Utilisation du mode 'a' pour ajouter sans écraser
        
        file.write(phrase + "\n")

while True:
    response = input("Souhaitez-vous ajouter des phrases à 'phrases.txt' ? (oui/non) : ").strip().lower()
    if response == "oui":
        ajouter_phrases()
    elif response == "non":
        print("Fin du programme.")
        break
