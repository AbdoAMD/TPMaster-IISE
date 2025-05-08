import os
import datetime
import math

current_directory = os.getcwd()
print(f"Répertoire courant : {current_directory}")

current_datetime = datetime.datetime.now()
print(f"Date et heure actuelles : {current_datetime}")

number = float(input("Entrez un nombre : "))
racine = math.sqrt(number)
print(f"La racine carrée de {number} est {racine}")
