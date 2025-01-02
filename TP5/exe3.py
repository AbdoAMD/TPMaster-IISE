def ajouter_phrases():
    
    reponse = input("Souhaitez-vous ajouter des phrases à 'phrases.txt' ? (oui/non) : ").lower()
    
    if reponse == "oui":
        while True:
            phrase = input("Entrez une phrase à ajouter : ")
            
            with open('phrases.txt', 'a') as file:
                file.write(phrase + "\n")
            
            continuer = input("Voulez-vous ajouter une autre phrase ? (oui/non) : ").lower()
            if continuer != "oui":
                break  
        
        print("Les phrases ont été ajoutées à 'phrases.txt'.")
    else:
        print("Aucune phrase n'a été ajoutée.")

ajouter_phrases()
