import pygame

class Piece () :
    def __init__(self,color:str,position:list,sprite_pathing :str,number_of_move:int):
        self.color = color
        self.position = position #as position [0] = y ; position[1] = x
        self.move_counter = number_of_move
        self.sprite_pathing = sprite_pathing
        self.sprite = pygame.transform.smoothscale(pygame.image.load(self.sprite_pathing).convert_alpha(),(60,60))
        self.movement_list = []

class Pawn (Piece):
    
    def __init__(self, color:str,position:list,sprite_pathing : str,number_of_move:int):
        super().__init__(color,position,sprite_pathing,number_of_move)
        self.name = "P"
    def move(self,grid:list,turn:str,list_of_play:list) -> list :
        """
        rules the pawn has to respect to move :
            -eat the Piece in a diagonal
            -en passant
            -can go two square forward in his first move
            -can go on one square forward if there is no Piece inside        

        Args:
            grid (list): the current grid with the pawn
            turn (string): the string of who has to play
            list_of_play (list): the list with all the moves played

        Returns:
            list: list of all the moves possible of the pawn
        """
        if self.color == turn:
            self.movement_list = []
            if self.color == "W": #if the pawn is white
                if self.position[0] == 6: #if the pawn is at his starting position
                    if grid[self.position[0]-1][self.position[1]] == None and grid[self.position[0]-2][self.position[1]] == None :
                        self.movement_list.append([self.position[0]-2,self.position[1]])#we had it playable board
                    
                if self.position[1] != 0 : #if the Piece is not next to the left side of the board
                    if grid[self.position[0]-1][self.position[1]-1] != None and grid[self.position[0]-1][self.position[1]-1].color == "B" : # if there is a black Piece 
                        self.movement_list.append([self.position[0]-1,self.position[1]-1]) #we had it playable board
                    if self.position[0] == 3 :
                        if len(list_of_play) != 0 :
                            if list_of_play[-1][0] == "P" and list_of_play[-1][1] == [self.position[0],self.position[1]-1] and grid[self.position[0]][self.position[1]-1].move_counter == 1:
                                self.movement_list.append([self.position[0]-1,self.position[1]-1])
                if self.position[1] != 7 : #if the Piece is not next to the left side of the board
                    if grid[self.position[0]-1][self.position[1]+1] != None and grid[self.position[0]-1][self.position[1]+1].color == "B" : # if there is a black Piece
                        self.movement_list.append([self.position[0]-1,self.position[1]+1]) #we had it playable board
                    if self.position[0] == 3 :
                        if len(list_of_play) != 0 :
                            if list_of_play[-1][0] == "P" and list_of_play[-1][1] == [self.position[0],self.position[1]+1] and grid[self.position[0]][self.position[1]+1].move_counter == 1:
                                self.movement_list.append([self.position[0]-1,self.position[1]+1])
                if grid[self.position[0]-1][self.position[1]] == None:
                    self.movement_list.append([self.position[0]-1,self.position[1]]) #if there is nothing in front of this pawn we had it to our movement grid
                    
            if self.color == "B":
                if self.position[0] == 1: #if the pawn is at his starting position
                    if grid[self.position[0]+1][self.position[1]] == None and grid[self.position[0]+2][self.position[1]] == None :
                        self.movement_list.append([self.position[0]+2,self.position[1]]) #we had it playable board
                    
                if self.position[1] != 0 : #if the Piece is not next to the right side of the board
                    if grid[self.position[0]+1][self.position[1]-1] != None and  grid[self.position[0]+1][self.position[1]-1].color == "W": # if there is a black Piece 
                        self.movement_list.append([self.position[0]+1,self.position[1]-1]) #we had it playable board
                    if self.position[0] == 4 :
                        if len(list_of_play) != 0 :
                            if list_of_play[-1][0] == "P" and list_of_play[-1][1] == [self.position[0],self.position[1]-1] and grid[self.position[0]][self.position[1]-1].move_counter == 1:
                                self.movement_list.append([self.position[0]+1,self.position[1]-1])
                if self.position[1] != 7: #if the Piece is not next to the left side of the board
                    if grid[self.position[0]+1][self.position[1]+1] != None and  grid[self.position[0]+1][self.position[1]+1].color == "W": # if there is a black Piece
                        self.movement_list.append([self.position[0]+1,self.position[1]+1]) #we had it playable board
                    if self.position[0] == 4 :
                        if len(list_of_play) != 0 :
                            if list_of_play[-1][0] == "P" and list_of_play[-1][1] == [self.position[0],self.position[1]+1] and grid[self.position[0]][self.position[1]+1].move_counter == 1:
                                self.movement_list.append([self.position[0]+1,self.position[1]+1])
                if grid[self.position[0]+1][self.position[1]] == None:
                    self.movement_list.append([self.position[0]+1,self.position[1]]) #if there is nothing in front of this pawn we had it to our movement grid

class Rook (Piece):
    def __init__(self, color:str,position:list,sprite_pathing:str,number_of_move:int):
        super().__init__(color,position,sprite_pathing,number_of_move)
        self.name = "R"
    def move(self,grid:list,turn:str,list_of_play:list) -> list :
        """ 
        rules the rook has to respect to move :
            -Eat pieces vertically and horizontally
            -can castling

        Args:
            grid (list): the current grid with the pawn
            turn (string): the string of who has to play
            list_of_play (list): the list with all the moves played

        Returns:
            list: list of all the moves possible of the pawn
        """
        if self.color == turn:
            self.movement_list = []
            self.tempory_move = [[],[]] #stock all the move before checking the color of the Piece, the first list is for all the x-axis move the second is for the y-axis move
            for pos,element in enumerate(grid[self.position[0]]):
                if pos<self.position[1]:
                    if element != None : #if it's not an empty square i clear the list
                        self.tempory_move[0].clear()
                    self.tempory_move[0].append([self.position[0],pos])
                elif pos>self.position[1]:
                    self.tempory_move[0].append([self.position[0],pos])
                    if element != None :
                        break
            for pos in range(len(grid)):
                if pos<self.position[0]:
                    if grid[pos][self.position[1]] != None : #if it's not an empty square I clear the list
                        self.tempory_move[1].clear()
                    self.tempory_move[1].append([pos,self.position[1]])
                elif pos>self.position[0]:
                    self.tempory_move[1].append([pos,self.position[1]])
                    if grid[pos][self.position[1]] != None :
                        break
                    
            if self.color == "W": #if the Piece is white we look for all the castles
                if self.position == [7,0] :
                    if self.move_counter == 0 :
                        if  isinstance(grid[7][4],King) :
                            if grid[7][4].move_counter == 0 :
                                if grid[7][1] == None and grid[7][2] == None and grid[7][3] == None :
                                    self.movement_list.append([7,4])
                if self.position == [7,7] :
                    if self.move_counter == 0 :
                        if isinstance(grid[7][4],King) :
                            if grid[7][4].move_counter == 0 :
                                if grid[7][5] == None and grid[7][6] == None:
                                    self.movement_list.append([7,4])
                for list in self.tempory_move:
                    for pos in list :
                        if grid[pos[0]][pos[1]] == None or grid[pos[0]][pos[1]].color =="B":
                            self.movement_list.append([pos[0],pos[1]])
                        
            elif self.color == "B": #if the Piece is Black we check for castle
                if self.position == [0,0] :
                    if self.move_counter == 0 :
                        if  isinstance(grid[0][4],King)  :
                            if grid[0][4].move_counter == 0 :
                                if grid[0][1] == None and grid[0][2] == None and grid[0][3] == None :
                                    self.movement_list.append([0,4])
                if self.position == [0,7] :
                    if self.move_counter == 0 :
                        if isinstance(grid[0][4],King)  :
                            if grid[0][4].move_counter == 0 :
                                if grid[0][5] == None and grid[0][6] == None:
                                    self.movement_list.append([0,4])
                for list in self.tempory_move:
                    for pos in list :
                        if grid[pos[0]][pos[1]] == None or grid[pos[0]][pos[1]].color =="W":
                            self.movement_list.append([pos[0],pos[1]])

class King (Piece):
    def __init__(self, color:str,position:list,sprite_pathing : str,number_of_move:int):
        super().__init__(color,position,sprite_pathing,number_of_move)
        self.name = "K"
    def move(self,grid:list,turn:str,list_of_play:list) :
        """ The king can move only one square around him
            or he can casling but only if the rook and the king haven't moove and no piece are between those two piece
        Args:
            grid (list): the grid 
            turn (str): who's turn
            list_of_play(list): the list of all the play
        """
        if self.color == turn:
            self.movement_list = []
            self.tempory_move = []
            self.tempory_move.append([self.position[0]-1,self.position[1]]) #we add all the possible direction 
            self.tempory_move.append([self.position[0]-1,self.position[1]-1])
            self.tempory_move.append([self.position[0]-1,self.position[1]+1])
            self.tempory_move.append([self.position[0],self.position[1]-1])
            self.tempory_move.append([self.position[0],self.position[1]+1])
            self.tempory_move.append([self.position[0]+1,self.position[1]-1])
            self.tempory_move.append([self.position[0]+1,self.position[1]+1])
            self.tempory_move.append([self.position[0]+1,self.position[1]])
            if self.color == "W":
                for position in self.tempory_move : #we check if the temporary position doesn't leave on a white Piece
                    if (position[0]<0 or position[0]>7) or (position[1]<0 or position[1]>7) :
                        continue
                    if grid[position[0]][position[1]] == None :
                        self.movement_list.append([position[0],position[1]])
                    elif grid[position[0]][position[1]].color == "B":
                        self.movement_list.append([position[0],position[1]])
            else :
                for position in self.tempory_move : #we check if the temporary position doesn't give on a black Piece
                    if (position[0]<0 or position[0]>7) or (position[1]<0 or position[1]>7) :
                        continue
                    if grid[position[0]][position[1]] == None :
                        self.movement_list.append([position[0],position[1]])
                    elif grid[position[0]][position[1]].color == "W":
                        self.movement_list.append([position[0],position[1]])

class Queen (Piece):
    def __init__(self, color:str,position:list,sprite_pathing : str,number_of_move:int):
        super().__init__(color,position,sprite_pathing,number_of_move)
        self.name = "Q"
    def move(self,grid:list,turn:str,list_of_play:list) :
        """
        the queen is the combination of all the move off the rook and the Bishop
        Args:
            grid (list): the grid
            turn (str): who's turn
            list_of_play(list): the list of all the play

        """
        if self.color == turn:
            self.movement_list = []
            self.tempory_move = [[],[],[],[]] #stock all the moves before checking the color of the Piece, the first list stock the diagonal move and the second the horizontal and vertical move
            for pos,element in enumerate(grid[self.position[0]]):
                if pos<self.position[1]:
                    if element != None : #if it's not an empty square I clear the list
                        self.tempory_move[2].clear()
                    self.tempory_move[2].append([self.position[0],pos])
                elif pos>self.position[1]:
                    self.tempory_move[2].append([self.position[0],pos])
                    if element != None :
                        break
            for pos in range(len(grid)):
                if pos<self.position[0]:
                    if grid[pos][self.position[1]] != None : #if it's not an empty square I clear the list
                        self.tempory_move[3].clear()
                    self.tempory_move[3].append([pos,self.position[1]])
                elif pos>self.position[0]:
                    self.tempory_move[3].append([pos,self.position[1]])
                    if grid[pos][self.position[1]] != None :
                        break
                            
                            
            self.wall_checker = False
            if self.color == turn:
                for y_axis in range(len(grid)):
                    for x_axis in range(len(grid[y_axis])):
                        if (x_axis-y_axis) == (self.position[1]-self.position[0]): # If this is true it does mean the Piece is on the same diagonal 
                            if self.position[1] > x_axis:
                                if grid[y_axis][x_axis] != None : #if it's not an empty square I clear the list
                                    self.tempory_move[0].clear()
                                self.tempory_move[0].append([y_axis,x_axis])
                            elif x_axis>self.position[1]:
                                self.tempory_move[0].append([y_axis,x_axis])
                                if grid[y_axis][x_axis] != None :
                                    self.wall_checker = True
                                    break
                    if self.wall_checker :
                        break
                wall_checker = False
                for y_axis in range(len(grid)):
                    for x_axis in range(len(grid[y_axis])) :
                        if (x_axis+y_axis) == (self.position[1]+self.position[0]):
                            if self.position[1]>x_axis:
                                self.tempory_move[1].append([y_axis,x_axis])
                                if grid[y_axis][x_axis] != None :
                                    wall_checker = True
                                    break
                            elif x_axis>self.position[1]:
                                if grid[y_axis][x_axis] != None : #if it's not an empty square I clear the list
                                    self.tempory_move[1].clear()
                                self.tempory_move[1].append([y_axis,x_axis])

                    if wall_checker :
                        break
                    
                    
                if self.color == "W" :
                    for list in self.tempory_move:
                        for pos in list :
                            if grid[pos[0]][pos[1]] == None or grid[pos[0]][pos[1]].color =="B":
                                self.movement_list.append([pos[0],pos[1]])
                else:
                    for list in self.tempory_move:
                        for pos in list :
                            if grid[pos[0]][pos[1]] == None or grid[pos[0]][pos[1]].color =="W":
                                self.movement_list.append([pos[0],pos[1]])

class Knight (Piece):
    def __init__(self, color:str,position:list,sprite_pathing : str,number_of_move:int):
        super().__init__(color,position,sprite_pathing,number_of_move)
        self.name = "N"
    def move(self,grid:list,turn:str,list_of_play:list) :
        """
            the knight moves in a "L" direction
        Args:
            grid (list): the actual grid 
            turn (str): who's turn
            list_of_play(list): the list of all the play
        """        
        if self.color == turn:
            self.movement_list = []
            self.tempory_move = []
            self.tempory_move.append([self.position[0]+2,self.position[1]+1])
            self.tempory_move.append([self.position[0]+2,self.position[1]-1])
            self.tempory_move.append([self.position[0]+1,self.position[1]+2])
            self.tempory_move.append([self.position[0]+1,self.position[1]-2])
            self.tempory_move.append([self.position[0]-2,self.position[1]+1])
            self.tempory_move.append([self.position[0]-2,self.position[1]-1])
            self.tempory_move.append([self.position[0]-1,self.position[1]+2])
            self.tempory_move.append([self.position[0]-1,self.position[1]-2])            
            
            if self.color == "W" :
                for pos in self.tempory_move:
                    if pos[0]<0 or pos[0]>7 or pos[1]<0 or pos[1]>7 :
                        continue
                    if grid[pos[0]][pos[1]] == None or grid[pos[0]][pos[1]].color =="B":
                        self.movement_list.append([pos[0],pos[1]])
            else:
                for pos in self.tempory_move:
                    if (pos[0]<0 or pos[0]>7) or (pos[1]<0 or pos[1]>7) :
                        continue
                    if grid[pos[0]][pos[1]] == None or grid[pos[0]][pos[1]].color =="W":
                        self.movement_list.append([pos[0],pos[1]])

class Bishop (Piece) :
    def __init__ (self, color:str,position:list,sprite_pathing : str,number_of_move:int):
        super().__init__(color,position,sprite_pathing,number_of_move)
        self.name = "B"
    def move(self,grid:list,turn:str,list_of_play:list) :
        """
        the bishop only moove in diagonal
        Args:
            grid (list): the grid
            turn (str): who's turn
            list_of_play(list): the list of all the plays played
        """
        if self.color == turn:
            self.movement_list = []
            self.wall_checker = False
            self.tempory_move = [[],[]] #stock all the moves before checking the color of the Piece, the first list is for all the diagonal →↓ move the second is for the diagonal →↑ move
            for y_axis in range(len(grid)):
                for x_axis in range(len(grid[y_axis])):
                    if (x_axis-y_axis) == (self.position[1]-self.position[0]): # If this is true it does mean the Piece is on the same diagonal 
                        if self.position[1] > x_axis:
                            if grid[y_axis][x_axis] != None : #if it's not an empty square I clear the list
                                self.tempory_move[0].clear()
                            self.tempory_move[0].append([y_axis,x_axis])
                        elif x_axis>self.position[1]:
                            self.tempory_move[0].append([y_axis,x_axis])
                            if grid[y_axis][x_axis] != None :
                                self.wall_checker = True
                                break
                if self.wall_checker :
                    break
            wall_checker = False
            for y_axis in range(len(grid)):
                for x_axis in range(len(grid[y_axis])) :
                    if (x_axis+y_axis) == (self.position[1]+self.position[0]):
                        if self.position[1]>x_axis:
                            self.tempory_move[1].append([y_axis,x_axis])
                            if grid[y_axis][x_axis] != None :
                                wall_checker = True
                                break
                        elif x_axis>self.position[1]:
                            if grid[y_axis][x_axis] != None : #if it's not an empty square I clear the list
                                self.tempory_move[1].clear()
                            self.tempory_move[1].append([y_axis,x_axis])

                if wall_checker :
                    break
            if self.color == "W" :
                for list in self.tempory_move:
                    for pos in list :
                        if grid[pos[0]][pos[1]] == None or grid[pos[0]][pos[1]].color =="B":
                            self.movement_list.append([pos[0],pos[1]])
            else:
                for list in self.tempory_move:
                    for pos in list :
                        if grid[pos[0]][pos[1]] == None or grid[pos[0]][pos[1]].color =="W":
                            self.movement_list.append([pos[0],pos[1]])

