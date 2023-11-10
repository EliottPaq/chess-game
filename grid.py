from piece import *
class grid :
    def __init__ (self):
        self.grid = [  # set the grid to the correct start position
            [Rock("B"),Knight("B"),Bishop("B"),Queen("B"),King("B"),Bishop("B"),Knight("B"),Rock("B")],
            [Pawn("B"),Pawn("B"),Pawn("B"),Pawn("B"),Pawn("B"),Pawn("B"),Pawn("B"),Pawn("B")],
            [None,None,None,None,None,None,None,None], 
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [Pawn("W"),Pawn("W"),Pawn("W"),Pawn("W"),Pawn("W"),Pawn("W"),Pawn("W"),Pawn("W")],
            [Rock("W"),Knight("W"),Bishop("W"),Queen("W"),King("W"),Bishop("W"),Knight("W"),Rock("W")]
            ]