import pygame

class piece () :
    def __init__(self,color:str,position:list(),sprite_pathing :str):
        self.color = color
        self.position = position #as position [0] = x ; position[1] = y
        self.sprite = pygame.transform.smoothscale(pygame.image.load(sprite_pathing).convert_alpha(),(60,60))
    def reset_movement_grid (self) :
        self.mouvement_grid = [  # set the grid to the correct start position
            [None,None,None,None,None,None,None,None], 
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None], 
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None]
            ]   
    #def checkmate(self,grid,turn):
        #if turn == self.color :
            

class Pawn (piece):
    
    def __init__(self, color:str,position:list,sprite_pathing : str):
        super.__init__(color,position,sprite_pathing)
    def __eq__(self) :
        return self.color
    def move(self,grid:list,turn:str,list_of_play:list) -> list :
        """
        rules the pawn have to respect to move :
            -eat piece in diagonale
            -en passant
            -can go two square forward in his first move
            -can go on one square forward if there is no piece inside        

        Args:
            grid (list): the current grid with the pawn
            turn (string) : the string of who have to play
            list_of_play (list) : the list with all the move played

        Returns:
            list: list of all the move possible of the pawn
        """
        self.reset_movement_grid (self)
        if self.color == turn:
            if self.color == "W": #if the pawn is white
                if self.position[0] != 6: #if the pawn is at his starting position
                    self.mouvement_grid[self.position[0]-2][self.position[1]] = True #we had it playable board
                    
                if self.position[1] != 0 : #if the piece is not next to the right side of the board
                    if grid[self.position[0]-1][self.position[1]-1] == "B"  : # if there is a black piece 
                        self.mouvement_grid[self.position[0]-1][self.position[1-1]] = True #we had it playable board
                    if self.position[0] == 2 : #if the piece is at the good place to "en passant"
                        if list_of_play[1][-1][0] == object(Pawn) and list_of_play[1][-1][1][0] == 3 and list_of_play[1][-1][1][1] == self.position[1]-1: #if the last move play by the black is pawn two sqare move next to the white pawn 
                            self.mouvement_grid[list_of_play[1][-1][1][0]][list_of_play[1][-1][1][1]] = True #we had that pawn to the mouvement grid
                            
                if self.position[1] != 7 : #if the piece is not next to the left side of the board
                    if grid[self.position[0]-1][self.position[1]+1] == "B" : # if there is a black piece
                        self.mouvement_grid[self.position[1]-1][self.position[0]+1] == True #we had it playable board
                    if self.position[0] == 2 : #if the piece is at the good place to "en passant"
                        if list_of_play[1][-1][0] == object(Pawn) and list_of_play[1][-1][1][0] == 3 and list_of_play[1][-1][1][1] == self.position[1]+1: #if the last move play by the black is pawn two sqare move next to the white pawn 
                            self.mouvement_grid[list_of_play[1][-1][1][0]][list_of_play[1][-1][1][1]] = True #we had that pawn to the mouvement grid
                        
                if grid[self.position[0]-1][self.position[1]] == None:
                    self.mouvement_grid[self.position[0]+1][self.position[1]] = True #if there is nothing in front of this pawn we had it to our mouvement grid
                    
            if self.color == "B":
                if self.position[0] != 1: #if the pawn is at his starting position
                    self.mouvement_grid[self.position[0]+2][self.position[1]] = True #we had it playable board
                    
                if self.position[1] != 0 : #if the piece is not next to the right side of the board
                    if grid[self.position[0]+1][self.position[1]-1] == "W"  : # if there is a black piece 
                        self.mouvement_grid[self.position[0]+1][self.position[1-1]] = True #we had it playable board
                    if self.position[0] == 5 : #if the piece is at the good place to "en passant"
                        if list_of_play[0][-1][0] == object(Pawn) and list_of_play[0][-1][1][0] == 4 and list_of_play[0][-1][1][1] == self.position[1]-1: #if the last move play by the black is pawn two sqare move next to the white pawn 
                            self.mouvement_grid[list_of_play[0][-1][1][0]][list_of_play[0][-1][1][1]] = True #we had that pawn to the mouvement grid
                            
                if self.position[1] != 7 : #if the piece is not next to the left side of the board
                    if grid[self.position[0]+1][self.position[1]+1] == "W" : # if there is a black piece
                        self.mouvement_grid[self.position[0]+1][self.position[1]+1] == True #we had it playable board
                    if self.position[0] == 5 : #if the piece is at the good place to "en passant"
                        if list_of_play[0][-1][0] == object(Pawn) and list_of_play[0][-1][1][0] == 4 and list_of_play[0][-1][1][1] == self.position[1]+1: #if the last move play by the black is pawn two sqare move next to the white pawn 
                            self.mouvement_grid[list_of_play[0][-1][1][0]][list_of_play[0][-1][1][1]] = True #we had that pawn to the mouvement grid
                        
                if grid[self.position[0]+1][self.position[1]] == None:
                    self.mouvement_grid[self.position[0]+1][self.position[1]] = True #if there is nothing in front of this pawn we had it to our mouvement grid


class Roock (piece):
    def __init__(self, color:str,position:list,sprite_pathing : str):
        super.__init__(color,position,sprite_pathing)
        self.move_counter = 0 

    def move(self,grid:list,turn:str,list_of_play:list) -> list :
        """ 
        rules the rook have to respect to move :
            -eat piece verticaly and horizontaly
            -can rock

        Args:
            grid (list): the current grid with the pawn
            turn (string) : the string of who have to play
            list_of_play (list) : the list with all the move played

        Returns:
            list: list of all the move possible of the pawn
        """
        if self.color == turn:
            self.tempory_move = [[],[]] #stock all the move before checking the color of the piece , the first list is for all the x axis move the second is for the y axis move
            for pos,element in enumerate(grid[self.postion[1]]):
                if pos<self.position[0]:
                    if element != None : #if it's not an empty square i clear the list
                        self.tempory_move[0].clear()
                    self.tempory_move[0].append([pos,self.position[1]])
                elif pos>self.position[0]:
                    self.tempory_move[0].append(pos,self.position[1])
                    if element != None :
                        break
            for pos in range(grid):
                if pos<self.position[1]:
                    if grid[pos][self.position[0]] != None : #if it's not an empty square i clear the list
                        self.tempory_move[1].clear()
                    self.tempory_move[1].append([self.position[0],pos])
                elif pos>self.position[1]:
                    self.tempory_move[1].append(self.position[0],pos)
                    if element != None :
                        break
                    
            if self.color == "W": #if the piece is white we look for all the castle
                if self.position == [7,0] :
                    if self.move_counter == 0 :
                        if grid[7][4] == object(King) :
                            if grid[7][4].move_counter == 0 :
                                if grid[7][1] == None and grid[7][2] == None and grid[7][3] == None :
                                    self.mouvement_grid[7][4] == True
                if self.position == [7,7] :
                    if self.move_counter == 0 :
                        if grid[7][4] == object(King) :
                            if grid[7][4].move_counter == 0 :
                                if grid[7][5] == None and grid[7][6] == None:
                                    self.mouvement_grid[7][4] == True
                for list in self.tempory_move:
                    for pos in list :
                        if grid[pos[0]][pos[1]] == None or grid[pos[0]][pos[1]].color =="B":
                            grid[pos[0]][pos[1]] == True
                        
            elif self.color == "B": #if the piece is Black we check for castle
                if self.position == [0,0] :
                    if self.move_counter == 0 :
                        if grid[0][4] == object(King) :
                            if grid[0][4].move_counter == 0 :
                                if grid[0][1] == None and grid[0][2] == None and grid[0][3] == None :
                                    self.mouvement_grid[0][4] == True
                if self.position == [0,7] :
                    if self.move_counter == 0 :
                        if grid[0][4] == object(King) :
                            if grid[0][4].move_counter == 0 :
                                if grid[0][5] == None and grid[0][6] == None:
                                    self.mouvement_grid[0][4] == True
                for list in self.tempory_move:
                    for pos in list :
                        if grid[pos[0]][pos[1]] == None or grid[pos[0]][pos[1]].color =="W":
                            grid[pos[0]][pos[1]] == True
                

class King (piece):
    def __init__(self, color:str,position:list,sprite_pathing : str):
        super.__init__(color,position,sprite_pathing)
        self.move_counter = 0 
    def move(self,grid:list,turn:str) :
        """the king can move only one square around him

        Args:
            grid (list): the grid 
            turn (str): who's turn
        """
        if self.color == turn:
            self.tempory_move = []
            self.tempory_move.append(self.position[0]-1,self.position[1]) #we add all the possible direction 
            self.tempory_move.append(self.position[0]-1,self.position[1]-1)
            self.tempory_move.append(self.position[0]-1,self.position[1]+1)
            self.tempory_move.append(self.position[0],self.position[1]-1)
            self.tempory_move.append(self.position[0],self.position[1]+1)
            self.tempory_move.append(self.position[0]+1,self.position[1]-1)
            self.tempory_move.append(self.position[0]+1,self.position[1]+1)
            self.tempory_move.append(self.position[0]+1,self.position[1])
        if self.color == "W":
            for position in self.tempory_move : #we chech if the tempory position doesn't give on a white piece
                if grid[position[0],position[1]] == None :
                    self.mouvement_grid[position[0]][position[1]] == True
                elif grid[position[0],position[1]].color == "B":
                    self.mouvement_grid[position[0]][position[1]] == True
        else :
            for position in self.tempory_move : #we chech if the tempory position doesn't give on a black piece
                if grid[position[0],position[1]] == None :
                    self.mouvement_grid[position[0]][position[1]] == True
                elif grid[position[0],position[1]].color == "W":
                    self.mouvement_grid[position[0]][position[1]] == True
        self.tempory_move.clear()
        
class Queen (Roock):
    def __init__(self, color:str,position:list,sprite_pathing : str):
        super.__init__(color,position,sprite_pathing)
    
    def move(self,grid:list,turn:str):
        """
        the queen is the combination of all the move off the rock and the Bishop
        Args:
            grid (list): the grid
            turn (str): who's turn
        """
        if self.color == turn:
            self.tempory_move = [[[],[]],[[],[]]] #stock all the move before checking the color of the piece ,the first list stock the diagonale moove and the second the horizontal and vertical move
            for y_axis in range(grid):
                for x_axis in range(grid[y_axis]) :
                    if (x_axis-y_axis) == (self.position[0]-self.position[1]):
                        if self.position[0]<x_axis:
                            if grid[y_axis][x_axis] != None : #if it's not an empty square i clear the list
                                self.tempory_move[0][0].clear()
                            self.tempory_move[0][0].append([x_axis,y_axis])
                        elif x_axis>self.position[0]:
                            self.tempory_move[0][0].append(x_axis,y_axis)
                            if grid[y_axis][x_axis] != None :
                                break
            for y_axis in range(grid):
                for x_axis in range(grid[y_axis]) :
                    if (x_axis+y_axis) == (self.position[0]+self.position[1]):
                        if self.position[1]>x_axis:
                            if grid[y_axis][x_axis] != None : #if it's not an empty square i clear the list
                                self.tempory_move[0][1].clear()
                            self.tempory_move[0][1].append([x_axis,y_axis])
                        elif x_axis<self.position[1]:
                            self.tempory_move[0][1].append(x_axis,y_axis)
                            if grid[y_axis][x_axis] != None :
                                break
                            
                            
            for pos,element in enumerate(grid[self.postion[1]]):
                if pos<self.position[0]:
                    if element != None : #if it's not an empty square i clear the list
                        self.tempory_move[1][0].clear()
                    self.tempory_move[1][0].append([pos,self.position[1]])
                elif pos>self.position[0]:
                    self.tempory_move[1][0].append(pos,self.position[1])
                    if element != None :
                        break
            for pos in range(grid):
                if pos<self.position[1]:
                    if grid[pos][self.position[0]] != None : #if it's not an empty square i clear the list
                        self.tempory_move[1][1].clear()
                    self.tempory_move[1][1].append([self.position[0],pos])
                elif pos>self.position[1]:
                    self.tempory_move[1][1].append(self.position[0],pos)
                    if element != None :
                        break
                    
                    
                    
            if self.color == "W" :
                for big_list in self.tempory_move:
                    for list in big_list:
                        for pos in list :
                            if grid[pos[0]][pos[1]] == None or grid[pos[0]][pos[1]].color =="B":
                                grid[pos[0]][pos[1]] == True
            else:
                for list in self.tempory_move:
                    for list in big_list:
                        for pos in list :
                            if grid[pos[0]][pos[1]] == None or grid[pos[0]][pos[1]].color =="W":
                                grid[pos[0]][pos[1]] == True


class Knight (piece):
    def __init__(self, color:str,position:list,sprite_pathing : str):
        super.__init__(color,position,sprite_pathing)
    
    def move(self,grid:list,turn:str):
        """
            the knight move in a "L" direction
        Args:
            grid (list): the actual grid 
            turn (str): who's turn
        """        
        if self.color == turn:
            self.tempory_move = []
            self.tempory_move.append(self.position[0]+2,self.position[1]+1)
            self.tempory_move.append(self.position[0]+2,self.position[1]-1)
            self.tempory_move.append(self.position[0]+1,self.position[1]+2)
            self.tempory_move.append(self.position[0]+1,self.position[1]-2)
            self.tempory_move.append(self.position[0]-2,self.position[1]+1)
            self.tempory_move.append(self.position[0]-2,self.position[1]+2)
            self.tempory_move.append(self.position[0]-1,self.position[1]+2)
            self.tempory_move.append(self.position[0]-1,self.position[1]-2)
            
            
            if self.color == "W" :
                for pos in self.tempory_move:
                    if grid[pos[0]][pos[1]] == None or grid[pos[0]][pos[1]].color =="B":
                        grid[pos[0]][pos[1]] == True
            else:
                for pos in self.tempory_move:
                    if grid[pos[0]][pos[1]] == None or grid[pos[0]][pos[1]].color =="W":
                        grid[pos[0]][pos[1]] == True

class Bishop (piece) :
    def __init__ (self, color:str,position:list,sprite_pathing : str):
        super.__init__(color,position,sprite_pathing)
    def move(self,grid:list,turn:str):
        """
        the bishop only moove in diagonale
        Args:
            grid (list): the grid
            turn (str): who's turn
        """
        if self.color == turn:
            self.tempory_move = [[],[]] #stock all the move before checking the color of the piece , the first list is for all the diagonal →↓ move the second is for the diagonal →↑ move
            for y_axis in range(grid):
                for x_axis in range(grid[y_axis]) :
                    if (x_axis-y_axis) == (self.position[0]-self.position[1]): # if this is true it does mean the piece is on the same diagonale 
                        if self.position[0]<x_axis:
                            if grid[y_axis][x_axis] != None : #if it's not an empty square i clear the list
                                self.tempory_move[0].clear()
                            self.tempory_move[0].append([x_axis,y_axis])
                        elif x_axis>self.position[0]:
                            self.tempory_move[0].append(x_axis,y_axis)
                            if grid[y_axis][x_axis] != None :
                                break
            for y_axis in range(grid):
                for x_axis in range(grid[y_axis]) :
                    if (x_axis+y_axis) == (self.position[0]+self.position[1]):
                        if self.position[1]>x_axis:
                            if grid[y_axis][x_axis] != None : #if it's not an empty square i clear the list
                                self.tempory_move[1].clear()
                            self.tempory_move[1].append([x_axis,y_axis])
                        elif x_axis<self.position[1]:
                            self.tempory_move[1].append(x_axis,y_axis)
                            if grid[y_axis][x_axis] != None :
                                break
            if self.color == "W" :
                for list in self.tempory_move:
                    for pos in list :
                        if grid[pos[0]][pos[1]] == None or grid[pos[0]][pos[1]].color =="B":
                            grid[pos[0]][pos[1]] == True
            else:
                for list in self.tempory_move:
                    for pos in list :
                        if grid[pos[0]][pos[1]] == None or grid[pos[0]][pos[1]].color =="W":
                            grid[pos[0]][pos[1]] == True
            
