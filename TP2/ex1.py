class Chien:
    def __init__(self, nom, race, age):
        self.nom = nom
        self.race = race
        self.age = age
# methode aboyer:        
    def aboyer(self):
       print("Woof!")

chien1 = Chien("Bobiz", "Pitbol", 7)
chien1.aboyer()