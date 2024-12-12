class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def se_presenter(self):
        print(f"Je suis {self.prenom} {self.nom}, j'ai {self.age} ans.")

class Etudiant(Personne):  
    def __init__(self, nom, prenom, age, matricule):
        super().__init__(nom, prenom, age)  
        self.matricule = matricule

    def etudier(self):
        print(f"je suis {self.prenom} {self.nom}, mon Matricule est : {self.matricule}")

personne = Personne("Abdelghani", "Amejoud", 25)
personne.se_presenter()

etudiant = Etudiant("Brahim", "Modan", 21, "D137849398")
etudiant.se_presenter()
etudiant.etudier()

