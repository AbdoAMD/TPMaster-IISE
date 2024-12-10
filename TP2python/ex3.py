class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self , montant):
        self.solde = self.solde + montant

    def retirer(self, montant):
        if (self.solde >= montant):
            self.solde = self.solde - montant
        else:
            print("Solde insuffisant")

    def afficher_solde(self):
        print("Solde de" , self.titulaire , " est :", self.solde, "DH")


compte = CompteBancaire("Abdelghani Amejoud", 1000)
compte.deposer(8000)
compte.retirer(3500)
compte.afficher_solde()
