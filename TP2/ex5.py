class Animal:
  def faire_du_bruit(self):
    print("Le bruit de l'animal")

class Chien(Animal):
  def faire_du_bruit(self):
    print("chien fait hoooow hoooow")

class Chat(Animal):
  def faire_du_bruit(self):
    print("chat fait Miau Miau")

chien = Chien()
chien.faire_du_bruit()
chat = Chat()
chat.faire_du_bruit()

