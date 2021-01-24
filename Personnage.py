from tkinter import Canvas
from AFF_Base import *

"""

Direction : 
    
     1
   2   3
     4

1 -> Nord, 2 -> Ouest, 3 -> Est, 4 -> Sud     
"""

class Personnage():
    def __init__(self):
        self.current_direction = 1
        self.new_direction = 1
        