# main.py

from src import addition, soustraction, multiplication, division
from src import concatener, mettre_en_majuscule

def main():
    print("Addition: ", addition(5, 3))
    print("Subtraction: ", soustraction(10, 4))
    print("Multiplication: ", multiplication(6, 7))
    print("Division: ", division(8, 2))

    print("Concatenate: ", concatener("Hello, ", "World!"))
    print("Uppercase: ", mettre_en_majuscule("hello"))

if __name__ == "__main__":
    main()
