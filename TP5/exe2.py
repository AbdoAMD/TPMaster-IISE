# Demander à l'utilisateur d'entrer trois phrases
phrase1 = input("Entrez la première phrase : ")
phrase2 = input("Entrez la deuxième phrase : ")
phrase3 = input("Entrez la troisième phrase : ")

with open('phrases.txt', 'w') as file:
    file.write(phrase1 + "\n")
    file.write(phrase2 + "\n")
    file.write(phrase3 + "\n")

print("Les phrases ont été enregistrées dans 'phrases.txt'.")
