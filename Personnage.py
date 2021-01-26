from tkinter import Canvas
from AFF_base import *

"""
Direction : 
    
     1
   2   3
     4

1 -> Nord, 2 -> Ouest, 3 -> Est, 4 -> Sud     
"""

class Personnage():
    def __init__(self, canvas):
        self.current_direction = 1
        self.new_direction = 1
        
        self.posx = 150
        self.posy = 150
        
        self.longueur = 30
        self.largeur = 30
        
        self.vitesse = 5 #En px/dep
        
    def PERDEP_Perso(self, canvas):
        if self.current_direction == 1:
            self.posy -= self.vitesse
        elif self.current_direction == 2:
            self.posx -= self.vitesse
        elif self.current_direction == 3:
            self.posx += self.vitesse
        else:
            self.posy += self.vitesse
            
        canvas.coords(self.sprite, AFF_TransCoord(self.posx, self.posy, self.longueur, self.largeur))
        
    