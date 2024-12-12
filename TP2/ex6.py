class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def surface(self):
        return self.largeur * self.hauteur

    def perimetre(self):
        return 2 * (self.largeur + self.hauteur)

rect = Rectangle(5, 10)
print(f"Surface : {rect.surface()}")
print(f"Périmètre : {rect.perimetre()}")

