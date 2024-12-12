class Chien:
    def __init__(self, nom, race, age):
        self.nom = nom
        self.race = race
        self.age = age
#creation methode aboyer:        
    def aboyer(self):
       print("Woof!")

# Exemple d'utilisation
chien1 = Chien("Abdelghani", "AMEJOUD", 24)
#print("Nom:", chien1.nom, "Race:", chien1.race, "Age:", chien1.age)
#chien1.aboyer()