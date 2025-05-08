from abc import ABC,abstractmethod  
class Animal(ABC):
    @abstractmethod
    def animal_parle(self):
        pass
class Chien(Animal) :
    def animal_parle(self):
        print("le chien Dir Wouffff")


class Chat(Animal):
    def animal_parle(self):
        print("la chat Dir Moiwwwwww")


chien=Chien()
chien.animal_parle()                 
chat=Chat()
chat.animal_parle() 