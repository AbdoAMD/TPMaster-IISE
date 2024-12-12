# Classe Livre
class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

# Classe Bibliotheque
class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, titre, auteur, annee_publication):
        livre = Livre(titre, auteur, annee_publication)
        self.livres.append(livre)

    def afficher_livres(self):
        for livre in self.livres:
            print(f"Titre: {livre.titre}, Auteur: {livre.auteur}, Année: {livre.annee_publication}")

# Test
bibliotheque = Bibliotheque()
bibliotheque.ajouter_livre("La Trilogie du Caire", "Naguib Mahfouz", 1988)
bibliotheque.ajouter_livre("Les Hommes dans le Soleil", "Ghassan Kanafani", 1992)
bibliotheque.ajouter_livre("Retour à Haïfa", "Ghassan Kanafani", 1948)

bibliotheque.afficher_livres()

