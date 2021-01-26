from tkinter import Canvas
from AFF_base import *
from Personnage import Personnage

class Fantome(Personnage):
    def __init__(self, canvas, couleur):
        super().__init__(canvas)
        self.sprite = AFF_Rectangle(canvas, self.posx, self.posy, self.longueur, self.largeur, fill=couleur)