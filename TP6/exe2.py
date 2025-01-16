
def convert_to_int(value):

    try:
        return int(value)
    except (ValueError, TypeError):
        raise ValueError(f"Erreur : Impossible de convertir '{value}' en entier.")

# Exemple d'utilisation

try:
        print(convert_to_int(7))
        print(convert_to_int('abdelghani'))  
except ValueError as e:
        print(e)  
