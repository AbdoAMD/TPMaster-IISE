class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.amis = []

    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.prenom} {self.nom} et j'ai {self.age} ans.")

    def ajouter_ami(self, ami):
        self.amis.append(ami)

    def afficher_amis(self):
        if self.amis:
            print("Mes amis sont :")
            for ami in self.amis:
                print(f" {ami.prenom} {ami.nom}")
        else:
            print("Je n'ai pas d'amis.")

# Test des fonctionnalités
p1 = Personne("Abdelghani", "Amejoud", 25)
p1.se_presenter()

p2 = Personne("Ahmed", "Samir", 24)
p1.ajouter_ami(p2)

p1.afficher_amis()
