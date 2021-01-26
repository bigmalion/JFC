from tkinter import *
from random import randrange
from affbases import *
c= "case"
m = "mur"
laby = [[c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c],
        [c,m,m,c,m,m,m,m,c,m,m,m,m,m,m,m,c,m,m,m,m,c,m,m,c,m,m,c,m,c],
        [c,c,c,c,m,m,m,m,c,c,c,c,c,c,c,c,c,c,c,c,c,c,m,m,c,c,c,c,c,c],
        [c,m,m,c,m,c,c,c,c,m,m,m,c,m,m,m,c,m,m,m,m,c,m,m,c,m,m,m,c,m],
        [c,m,m,c,m,c,m,m,c,m,m,m,c,m,m,m,c,m,m,m,m,c,m,m,c,m,m,m,c,m],
        [c,c,c,c,m,c,c,m,c,m,m,m,c,m,m,m,c,m,m,m,m,c,m,m,c,m,c,c,c,m],
        [m,m,m,c,m,m,m,m,c,m,m,m,c,m,m,m,c,m,m,m,m,c,m,m,c,m,m,m,c,m],
        [c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c],
        [c,m,m,c,m,m,m,m,m,c,m,c,m,m,m,c,m,c,m,c,m,c,m,m,m,m,c,m,m,c],
        [c,c,c,c,c,c,c,c,c,c,m,c,c,c,c,c,m,c,c,c,m,c,c,c,c,c,c,c,c,c]]


fen1 = Tk()
can1 = Canvas(fen1 , bg="white", width = 900, height=300)
can1.pack()


def radjacent(x,y):
    """Rend dans l'ordre le nuémro de la case de gauche  , de droite , du desus et
    du bas en donnant la position x y du centre de pac man"""

    i = rcase(x,y)[0]
    j = rcase(x,y)[1]
    if (j-1)>=0:
        gauche = laby[i][j-1]
    else:
        gauche = "mur"
    if (j+1)<= 29:
        droite = laby[i][j+1]
    else:
        droite = "mur"
    if (i-1)>=0:
        haut = laby[i-1][j]
    else:
        haut = "mur"
    if (i+1)<=9:
        bas = laby[i+1][j]
    else:
        bas = "mur"
    return gauche,droite,haut,bas



def rcase(x,y):
    """sert uniquement a revoyer l'adresse de la case (utiliser dans la fonction radjacent """
    casei = int(x/30)
    casej = int(y/30)
    return casei,casej

def AFF_laby(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == "case":
                AFF_Rectangle(can1,i15, j15, 30, 30, fill="blue")


AFF_laby(laby)



print(radjacent(15,15))