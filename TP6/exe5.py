def process_input(user_input):
    try:
        result = float(user_input) / 10
        print("Résultat de la division par 10 : ", result)
    except ValueError:
        print("Erreur : l'entrée n'est pas un nombre valide.")
    except ZeroDivisionError:
        print("Erreur : division par zéro.")
process_input("20")  # Affichera : Résultat de la division par 10 : 10.0
process_input("abbdelghani")  
process_input("0")    
