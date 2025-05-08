""" with open("exempl.txt", "r") as fichier:
    contenu = fichier.readlines()
    print(contenu)

for x, line in enumerate(contenu, 1):
        print( "Ligne" ,x, line.strip()) """


"""
#exercice2
phrase1=input("Entrez la 1ere phrase: ")
phrase2=input("Entrez la 2eme phrase: ")
phrase3=input("Entrez la 3eme phrase: ")

with open("Abdelghani.txt", "w") as file:
    file.write(phrase1 + "\n")
    file.write(phrase2+ "\n")
    file.write(phrase3+ "\n")

print("Tout les phrases sont ajouter a le file")    """

""""
#exercice3
def ajouter_phrases():
    phrase = input("Entrez une phrase: ")
    with open("Abdelghani.txt", "w") as file:  # Utilisation du mode 'a' pour ajouter sans écraser
        
        file.write(phrase + "\n")

while True:
    response = input("Souhaitez-vous ajouter des phrases à 'Abdelghani.txt' ? (oui/non) : ").strip().lower()
    if response == "oui":
        ajouter_phrases()
    elif response == "non":
        print("Fin du programme.")
        break
        
      """

#exercice1
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
        Personne.__init__(nom,prenom,ID)
        self.salaire = salaire
        self.departement = departement
    def afficher_info(self):
        print(super().afficher_info(),"Salaire :",self.salaire,"Departement :",self.departement)
    def augment_salaire(self,pourcentage):
        self.salaire = self.salaire * pourcentage /100
        print("Nouvelle salaire apres l'augmentation est :" ,self.salaire)
#################################3
class Departement:
    def __init__(self,nom,list_employees):
        self.nom = nom
        self.list_employees = list_employees
    def ajouter_employe(self,employe):
        self.list_employees.append(employe)
    
    def afficher_employe(self):
        print("la liste des emplyee de ",self.nom,"est :")
        for x in self.list_employees:
            print(x)
#######################################
class projet:
    def __init__(self,nom, budget,list_employees_assigee):
        self.nom = nom
        self.budget = budget
        self.list_employees_assigee = list_employees_assigee
    def ajouter_emplye(self,employee):
        self.list_employees_assigee.append(employee)
    def afficher_info(self):
        print("Le nom de projet",self.nom)
        print("Le Budget de projet",self.budget)
        print("La liste des employees de projet: ")
        for x in self.list_employees_assigee:
            print(x)        
################################
#Gestion des Exceptions
class EmployeInvalide(Exception):
    pass
class DepartementInvalide(Exception):
    pass
##########################################3
#Gestion des Fichiers (Sauvegarde et Chargement en JSON)
import json
def sauvegarder_donnees(fichier, donnees):
    with open(fichier, 'w') as f:
        json.dump(donnees, f, indent=4)

def charger_donnees(fichier):
    try:
        with open(fichier, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
