# Exception personnalisée simplifiée
class NegativeAgeError(Exception):
   pass
# Fonction pour définir l'âge
def set_age(age):
    if age < 0:
        raise NegativeAgeError("Erreur : L'âge ne peut pas être négatif.")
    print(f"Âge défini avec succès : {age}")

try:
    set_age(25)  
    set_age(-5)  
except NegativeAgeError as e:
    print(e)