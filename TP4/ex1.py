class Vehicule:
    def __init__(self,marque,modele,annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
    def afficher_info(self):
        print("Marque: ",self.marque,"modele: ",self.modele,"Annee: ",self.annee)  

class Moteur:
    def __init__(self,puissance,type_moteur):
        self.puissance = puissance
        self.type_moteur = type_moteur

    def afficher_moteur(self):
        print("Puissance: ",self.puissance,"Type_moteur: ",self.type_moteur)


class Voiture(Vehicule,Moteur):
    def __init__(self,marque,modele,annee,puissance,type_moteur,nombre_de_places):
        Vehicule.__init__(self,marque,modele,annee)
        Moteur.__init__(self,puissance,type_moteur)
        self.nombre_de_places = nombre_de_places

    def afficher_info(self):
        print(super().afficher_info(),super().afficher_moteur(),"Nombre de places est: ",self.nombre_de_places)


class Moto(Vehicule,Moteur):
    def __init__(self,marque,modele,annee,puissance,type_moteur,type_moto):
        Vehicule.__init__(self,marque,modele,annee)
        Moteur.__init__(self,puissance,type_moteur)
        self.type_moto = type_moto

    def afficher_info(self):
        print(super().afficher_info(),"Puissance : ",self.puissance,"Type_moteur: ",self.type_moteur,"Type de moto est: ",self.type_moto)


voiture=Voiture("Toyota", "Corolla", 2020, 130, "Essence", 5)        
moto = Moto("Yamaha", "MT-07", 2022, 74, "Essence", "Sport")


print("Informations de la voiture:")
voiture.afficher_info()

print("\nInformations de la moto:")
moto.afficher_info()


