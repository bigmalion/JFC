from tkinter import *
from Personnage import Personnage 
from Pacman import Pacman
from Fantome import Fantome

def INIT_pacman(fenetre, canvas):
    pacman = Pacman(canvas)
    for k in ["<Down>", "<Left>", "<Right>", "<Up>"]:
        fenetre.bind(k, pacman.PERDEP_ChgNewDir)
    return pacman

def INIT_fantome(canvas):
    fantomes = []
    for c in ["purple", "blue", "orange"]:
        fantomes.append(Fantome(canvas, c))
    return fantomes

def LOOP_pacman(pacman, canvas):
    pacman.current_direction = pacman.new_direction
    pacman.PERDEP_Perso(canvas)
    
def LOOP_fantome(fantome, canvas):
    for fant in fantome:
        fant.PERDEP_Perso(canvas)