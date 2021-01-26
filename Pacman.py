from tkinter import Canvas
from AFF_base import *
from Personnage import Personnage
 
class Pacman(Personnage):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.sprite = AFF_Cercle(canvas, self.posx, self.posy, self.longueur, fill="yellow")
        
    def PERDEP_ChgNewDir(self, event):
        if event.keysym == "Right":
            self.new_direction = 3
        elif event.keysym == "Left":
            self.new_direction = 2
        elif event.keysym == "Down":
            self.new_direction = 4
        elif event.keysym == "Up":
            self.new_direction = 1
        
        
    
