# Classe Personne
class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def se_presenter(self):
        print( "Je suis {self.prenom} {self.nom}, j'ai {self.age} ans.")

# Sous-classe Etudiant
    def Etudiant(Personne):  
        self.Personne = Personne()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def etudier(self):
        print(f"{self.prenom} étudie. Matricule : {self.matricule}")

# Test des classes
personne = Personne("abdelghani", "amejoud", 25)
personne.se_presenter()

etudiant = Etudiant("brahim", "farhan", 21, "A123")
etudiant.se_presenter()
etudiant.etudier()
