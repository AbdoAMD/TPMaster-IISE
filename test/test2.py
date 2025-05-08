"""A=int(input("entrez la valeure de A :"))
B=int(input("entrez la valeure de B :"))

def division(A,B):
    if B==0:
        raise ZeroDivisionError("la division par zero imposible")
    else:
        return  A / B
           

try:
    res=division(A,B)
    print("la division est:",res)
except ZeroDivisionError as e:
    print(e)"""
class Personne:
    def __init__(self,nom,prenom,ID):
        self.nom = nom
        self.prenom = prenom
        self.ID = ID
    def afficher_info(self):
        print ("les information de cette Personne sont: \n","Nom :",self.nom,"Prenom :",self.prenom,"ID :",self.ID)   
##########################
class Employee(Personne):
    def __init__(self,nom,prenom,ID,salaire,departement):
        super().__init__(nom,prenom,ID)
        self.salaire = salaire
        self.departement = departement
    def afficher_info(self):
        print(super().afficher_info(),"Salaire :",self.salaire,"DH","Departement :",self.departement)
    def augment_salaire(self,pourcentage):
        augmentation = self.salaire * pourcentage /100
        self.salaire = self.salaire + augmentation
        print("Nouvelle salaire apres l'augmentation est :" ,self.salaire,"dh")

emmplyee=Employee("Ahmed","sadik",2123,2000,"informatique")
emmplyee.afficher_info()
emmplyee.augment_salaire(5)
      