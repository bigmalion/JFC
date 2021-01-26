from tkinter import *
from Personnage import Personnage 
from Pacman import Pacman
from Fantome import Fantome
from Base_Perso import *

fenetre = Tk()

can = Canvas(fenetre, width = 900, height = 300)
can.pack()

pacman = INIT_pacman(fenetre, can)
fantomes = INIT_fantome(can)

#Deboguage
deb_label1 = Label(fenetre, text="Posx : unknow | Posy : unknow")
deb_label1.pack(side=TOP)

def MainLoop():
    LOOP_pacman(pacman, can)
    LOOP_fantome(fantomes, can)
    fenetre.after(25, MainLoop)
    #Deboguage
    deb_label1.configure(text="Posx :"+str(pacman.posx)+"| Posy : "+str(pacman.posy))
    
    
fenetre.after(25, MainLoop)

fenetre.mainloop()