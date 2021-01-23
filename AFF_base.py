from tkinter import Canvas

def AFF_TransCoord(x: int, y:int, longueur:int, largeur:int, **arguments):
    """Paramètre :
    - x l'abcisse du centre de la figure voulut
    - y l'ordonné du centre de la figure voulut
    - largeur la largeur de la figure voulut
    - longueur la longueur de la figure voulut
    - arguments le dictionnaire contenant toutes les informations supplémentaires pour la figure
    """
    return int(x-longueur/2),int(y-largeur/2),int(x+longueur/2),int(y+largeur/2), arguments

def AFF_Rectangle(canvas,x:int, y:int, longueur:int, largeur:int, **arguments):
    """
    Creer un rectangle
    
    Paramètre :
    - canvas le canvas ou doit etre creer le rectangle
    - x l'abcisse du centre du rectangle voulut
    - y l'ordonné du centre du rectangle voulut
    - largeur la largeur du rectangle voulut
    - longueur la longueur du rectangle voulut
    - arguments le dictionnaire contenant toutes les informations supplémentaires pour le rectangle
    
    Retourne : l'adresse memoire du rectangle
    """
    return canvas.create_rectangle(AFF_TransCoord(x, y, longueur, largeur, **arguments))

def AFF_Cercle(canvas,x:int, y:int, rayon:int, **arguments)-> list:
    """
    Creer un cercle
    
    Paramètre :
    - canvas le canvas ou doit etre creer le cercle
    - x l'abcisse du centre du cercle voulut
    - y l'ordonné du centre du cercle voulut
    - rayon le rayon du cercle
    - arguments le dictionnaire contenant toutes les informations supplémentaires pour le cercle
    
    Retourne : l'adresse memoire du cercle
    """
    return canvas.create_oval(AFF_TransCoord(x, y, rayon*2, rayon*2, **arguments))

