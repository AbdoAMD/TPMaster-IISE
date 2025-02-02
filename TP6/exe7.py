import logging

# Configuration du logging pour enregistrer les erreurs dans error.log
logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,  # Nous nous intéressons seulement aux erreurs
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_error(message):
    """
    Fonction qui enregistre un message d'erreur dans le fichier error.log
    """
    logging.error(message)

# Exemple d'exercice modifié pour utiliser log_error
def read_file(file_path):
   
    try:
        with open(file_path ,'r') as file:
            return file.read()
    except FileNotFoundError:
        log_error(f"Le fichier '{file_path}' n'a pas été trouvé.")
        

#Exemple d'utilisation
resultat= read_file('inexistant.txt')
if resultat is None:
    print("Une erreur est survenue, consultez error.log pour plus de détails.")
