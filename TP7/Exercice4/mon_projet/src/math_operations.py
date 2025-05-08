def addition(a, b):
    """
    Additionne deux nombres.

    Parameters:
    a (int, float): Le premier nombre.
    b (int, float): Le deuxième nombre.

    Returns:
    int, float: La somme des deux nombres.
    """
    return a + b

def soustraction(a, b):
    """
    Soustrait le deuxième nombre du premier.

    Parameters:
    a (int, float): Le premier nombre.
    b (int, float): Le deuxième nombre.

    Returns:
    int, float: La différence entre les deux nombres.
    """
    return a - b

def multiplication(a, b):
    """
    Multiplie deux nombres.

    Parameters:
    a (int, float): Le premier nombre.
    b (int, float): Le deuxième nombre.

    Returns:
    int, float: Le produit des deux nombres.
    """
    return a * b

def division(a, b):
    """
    Divise le premier nombre par le deuxième.

    Parameters:
    a (int, float): Le premier nombre.
    b (int, float): Le deuxième nombre.

    Returns:
    int, float: Le quotient des deux nombres.

    Raises:
    ZeroDivisionError: Si le deuxième nombre (b) est égal à zéro.
    """
    if b == 0:
        raise ZeroDivisionError("Impossible de diviser par zéro")
    return a / b
