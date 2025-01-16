def safe_division(a, b):
    if b == 0:
        raise ZeroDivisionError("Erreur : Impossible de diviser par zéro.")
    return a / b

try:
    result = safe_division(10, 2)  
    print("Résultat de la division :", result)
except ZeroDivisionError as e:
    print(e)
else:
    print("La division a été effectuée avec succès.")

finally:

    print('la fin de la fonction ')



 
