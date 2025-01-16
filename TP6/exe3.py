def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("Contenu du fichier :")
            print(content)
    except FileNotFoundError:
        print("Erreur : Le fichier" + filename +" n'existe pas.")

read_file('exemple.txt')

read_file("fichier_inexistant.txt")     
