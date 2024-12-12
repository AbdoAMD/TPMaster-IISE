class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_info(self):
        print("Voiture: ",self.marque, self.modele,"Année: ", self.annee)

voiture1 = Voiture("Toyota", "Corolla", 2020)
voiture2 = Voiture("Honda", "Civic", 2018)
voiture3 = Voiture("Ford", "Focus", 2019)

voiture1.afficher_info()
voiture2.afficher_info()
voiture3.afficher_info()
