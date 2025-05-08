class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    # Getters
    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def get_age(self):
        return self.age

    # Setters
    def set_nom(self, nom):
        self.nom = nom

    def set_prenom(self, prenom):
        self.prenom = prenom

    def set_age(self, age):
        if age > 0:
            self.age = age
        else:
            print("L'âge doit être un nombre positif.")


personne = Personne("Dupont", "Pierre", 30)
print(personne.get_nom())  
print(personne.get_prenom()) 
print(personne.get_age()) 

personne.set_age(35)
print(personne.get_age())  


personne.set_age(-5)  
