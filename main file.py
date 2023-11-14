import pygame
from sys import exit
import copy
def print_board () :
    """
    this function just print the grid (white and black square)
    """    
    
    axis_value = [0,75,150,225,300,375,450,525] #those value are the limit of each square in x and y axis
    color_value = 0 #this value is need to set a variable color
    for y in axis_value :
        for x in axis_value :
            if color_value == 0 :
                pygame.draw.rect(screen,"white",[x,y,75,75]) #75,75 is the height and length of each square
                if x != 525 :# at the last rectangle we are not changing the color because otherwise it wouldnt be a real chess board
                    color_value = 1
            elif color_value== 1 :
                pygame.draw.rect(screen,"black",[x,y,75,75]) #75,75 is the height and length of each square
                if x != 525:
                    color_value = 0# at the last rectangle we are not changing the color because otherwise it wouldnt be a real chess board

def print_piece (grid:list) :
    """
    this function is adding the piece on the board
    Args:
        grid (list): it's the list who contain all our piece
    """    
    
    axis_value = [0,75,150,225,300,375,450,525]#those value are the limit of each square in x and y axis
    for row_number,row in enumerate(grid):
        for column,piece in enumerate(row) :
            if piece[0] == "W":
                if piece[1] == "T" :
                    white_tower_surf = white_tower_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5)) # 37.5 is the half of 37.5 by using this value we are placing our piece in the middle of each square
                    screen.blit(white_tower_sprite,white_tower_surf)
                if piece[1] == "N" :
                    white_knight_surf = white_knight_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5)) # 37.5 is the half of 37.5 by using this value we are placing our piece in the middle of each square
                    screen.blit(white_knight_sprite,white_knight_surf)
                if piece[1] == "B" :
                    white_bishop_surf = white_bishop_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5)) # 37.5 is the half of 37.5 by using this value we are placing our piece in the middle of each square
                    screen.blit(white_bishop_sprite,white_bishop_surf)
                if piece[1] == "Q" :
                    white_queen_surf = white_queen_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5)) # 37.5 is the half of 37.5 by using this value we are placing our piece in the middle of each square
                    screen.blit(white_queen_sprite,white_queen_surf)
                if piece[1] == "K" :
                    white_king_surf = white_king_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5)) # 37.5 is the half of 37.5 by using this value we are placing our piece in the middle of each square
                    screen.blit(white_king_sprite,white_king_surf)
                if piece[1] == "P" :
                    white_pawn_surf = white_pawn_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5)) # 37.5 is the half of 37.5 by using this value we are placing our piece in the middle of each square
                    screen.blit(white_pawn_sprite,white_pawn_surf)
            elif piece[0] =="B" :
                if piece[1] == "T" :
                    black_tower_surf = black_tower_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5)) # 37.5 is the half of 37.5 by using this value we are placing our piece in the middle of each square
                    screen.blit(black_tower_sprite,black_tower_surf)
                if piece[1] == "N" :    
                    black_knight_surf = black_knight_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5)) # 37.5 is the half of 37.5 by using this value we are placing our piece in the middle of each square
                    screen.blit(black_knight_sprite,black_knight_surf)
                if piece[1] == "B" :
                    black_bishop_surf = black_bishop_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5)) # 37.5 is the half of 37.5 by using this value we are placing our piece in the middle of each square
                    screen.blit(black_bishop_sprite,black_bishop_surf)
                if piece[1] == "Q" :
                    black_queen_surf = black_queen_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5)) # 37.5 is the half of 37.5 by using this value we are placing our piece in the middle of each square
                    screen.blit(black_queen_sprite,black_queen_surf)
                if piece[1] == "K" :
                    black_king_surf = black_king_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5)) # 37.5 is the half of 37.5 by using this value we are placing our piece in the middle of each square
                    screen.blit(black_king_sprite,black_king_surf)
                if piece[1] == "P" :
                    black_pawn_surf = black_pawn_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5)) # 37.5 is the half of 37.5 by using this value we are placing our piece in the middle of each square
                    screen.blit(black_pawn_sprite,black_pawn_surf)

def where_am_i (mouse_pos:list):
    """
    we are transforming the mouse_pos in a place in our grid who is readable

    Args:
        mouse_pos (list): our mouse position [x,y]

    Returns:
        list: the position of our mouse in the grid
    """    
    
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    x = -1
    y= -1
    while mouse_x >= 0:
        x += 1
        mouse_x -= 75
    while mouse_y >= 0 : 
        y += 1
        mouse_y -= 75
    return [y,x]

    def show_possibilty(grid:list,position:list,turn):
        """
        we are taking our grid,our position , and the turn to know where the piece which we click on can go 

        Args:
            grid (list): the grid of the game
            position (list): the position of the mouse
            turn (int): who's turn (white or black)

        Returns:
            list : a list who contain a grid of all the place the piece can go (Y are for "the piece can go there)
        """        
        
    mouvement_grid = [
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],   
    ]
    #this "mouvement_grid" will be modifying she will contain all the place the piece can go
    plays,selected_piece = mouvement(grid,position,turn) #we need mouvement function which will give us all the position of the piece can go
    for play in plays :
        mouvement_grid[play[0]][play[1]] = "Y" #transforming empty slot into "Y"
    return selected_piece,mouvement_grid

def mouvement(grid:list,position:list,turn:int) :
    """
    we analyse the grid , the position and ,who's turn is to return a list with all the moove the piece who is choose can go
    Args:
        grid (list): our chess board
        position (list): the position of the piece clicked
        turn (int): who's turn (white or black)

    Returns:
        list: a list with the moove of the piece
    """    
    
    piece = grid[position[0]][position[1]] # piece is the piece who is click on it's a string who's first letter is "W" or "B" for the colour and the second letter is the type of piece ("T" for rook/tower,"B" for bishop,"N" for knight,"Q" for queen,"K"for king,"P" for pawn)
    type_of_piece = piece[1] # we are storing the type of our piece
    color_of_piece = piece[0] # we are storing the colour of our piece
    plays_allowed = [] # those are usefull  
    plays_tempory_allowed = []
    stock_of_play = []
    final_play = []
    
    if type_of_piece == "T" or type_of_piece == "Q": #if the piece is a rook/tower or a queen
        wall = True 
        for x_value,piece in enumerate(grid[position[0]]): #we are analysing the line where the tower is
            if wall == True :
                    if piece == "--":
                        plays_tempory_allowed.append([position[0],x_value]) #if it's an empty slot we add into the list
                    else: #if it's not an empty slot
                        if x_value < position[1]: #if the  wall is before (in term of list reading) the rook/tower
                            plays_tempory_allowed.clear() # we are deleting all the value because the wall stop the rook/tower
                            plays_tempory_allowed.append([position[0],x_value]) # we add the piece who block us
                        if x_value > position[1]: # if the wall is after the rook/tower
                            plays_tempory_allowed.append([position[0],x_value]) #we add the piece
                            wall = False # set this value to stop the line reading
            
        for plays in plays_tempory_allowed:
            plays_allowed.append(plays) #we are adding all the moove we choose before into a almost final list
        plays_tempory_allowed.clear() #empty this list

        # we know how add the play of a rook for the line it's not different for the column
        for line in range(len(grid)):
            stock_of_play.append(grid[line][position[1]]) #we are "transforming" our column into a list 
        #we do the exact same thing we do for the line
        wall = True 
        for y_value,piece in enumerate(stock_of_play):
            if wall == True :
                if piece == "--":
                    plays_tempory_allowed.append([y_value,position[1]])
                else:
                    if y_value < position[0]:
                        plays_tempory_allowed.clear()
                        plays_tempory_allowed.append([y_value,position[1]])
                    if y_value > position[0]:
                        plays_tempory_allowed.append([y_value,position[1]])
                        wall = False
        for plays in plays_tempory_allowed:
            plays_allowed.append(plays)
        plays_tempory_allowed.clear()
        wall = True
        stock_of_play.clear()
    if type_of_piece == "B" or type_of_piece == "Q": # if the piece is a bishop or a queen
        
            wall = True
            stock_of_play = diagonale_right(position) # we are calling a function who give us a list of the diagonale who go like this →↓ 
            # we do the same thing we for the line of the rook
            for play in stock_of_play:
                if wall == True :
                    if grid[play[0]][play[1]] == "--":
                        plays_tempory_allowed.append(play)
                    else:
                        if play[1] < position[1]:
                            plays_tempory_allowed.clear()
                            plays_tempory_allowed.append(play)
                        if play[1] > position[1]:
                            plays_tempory_allowed.append(play)
                            wall = False
                    
            for plays in plays_tempory_allowed:
                plays_allowed.append(plays)
            plays_tempory_allowed.clear()
            
            stock_of_play = diagonale_left(position) # we are calling a function who give us a list of the diagonale who go like this →↑ 
            wall = True
            #and again same strategy 
            for play in stock_of_play:
                if wall == True :
                    if grid[play[0]][play[1]] == "--":
                        plays_tempory_allowed.append(play)
                    else:
                        if play[1] < position[1]:
                            plays_tempory_allowed.clear()
                            plays_tempory_allowed.append(play)
                        if play[1] > position[1]:
                            plays_tempory_allowed.append(play)
                            wall = False
            for plays in plays_tempory_allowed:
                plays_allowed.append(plays)
            plays_tempory_allowed.clear()
    stock_of_play.clear()
    
    if type_of_piece == "K":
        #the king can go eveywhere around him but one square long
        plays_allowed.append([position[0]+1,position[1]+1])
        plays_allowed.append([position[0],position[1]+1])
        plays_allowed.append([position[0]+1,position[1]])
        plays_allowed.append([position[0],position[1]-1])
        plays_allowed.append([position[0]-1,position[1]])
        plays_allowed.append([position[0]-1,position[1]+1])
        plays_allowed.append([position[0]+1,position[1]-1])
        plays_allowed.append([position[0]-1,position[1]-1])
    if type_of_piece == "N":
        #knight can go in "L"
        plays_allowed.append([position[0]+2,position[1]+1])
        plays_allowed.append([position[0]+2,position[1]-1])
        plays_allowed.append([position[0]-2,position[1]+1])
        plays_allowed.append([position[0]-2,position[1]-1])
        plays_allowed.append([position[0]+1,position[1]+2])
        plays_allowed.append([position[0]+1,position[1]-2])
        plays_allowed.append([position[0]-1,position[1]-2])
        plays_allowed.append([position[0]-1,position[1]+2])
    if type_of_piece == "P":
            if turn == 0:
                if grid[position[0]-1][position[1]] == "--" :
                    plays_allowed.append([position[0]-1,position[1]])  
                if position[0] == 6 and grid[position[0]-2][position[1]] == "--":
                    plays_allowed.append([position[0]-2,position[1]])
                if position[1] != 0 :
                    if grid[position[0]-1][position[1]-1][0] == "B":
                        plays_allowed.append([position[0]-1,position[1]-1])
                if position[1] != 7 :
                    if grid[position[0]-1][position[1]+1][0] == "B":
                        plays_allowed.append([position[0]-1,position[1]+1])
            else :
                if grid[position[0]+1][position[1]] == "--" :
                    plays_allowed.append([position[0]+1,position[1]])
                if position[0] == 1 and grid[position[0]+2][position[1]] == "--":
                    plays_allowed.append([position[0]+2,position[1]])
                if position[1] != 0 :
                    if grid[position[0]+1][position[1]-1][0] == "W":
                        plays_allowed.append([position[0]+1,position[1]-1])
                if position[1] != 7 :
                    if grid[position[0]+1][position[1]+1][0] == "W":
                        plays_allowed.append([position[0]+1,position[1]+1])
    if turn == 0 :
        for play in plays_allowed :
            if play[0] >= 0 and play[0] < 8 and play[1] >= 0 and play[1] < 8: #we delete every number who are not in the grid
                if color_of_piece=="W": 
                    if grid[play[0]][play[1]][0] != "W" : #we don't go in a spot who is the same color
                        final_play.append(play)
    else :
        for play in plays_allowed :
            if play[0] >= 0 and play[0] < 8 and play[1] >= 0 and play[1] < 8:  #we delete every number who are not in the grid
                if color_of_piece=="B":
                    if grid[play[0]][play[1]][0] != "B" : #we don't go in a spot who is the same color
                        final_play.append(play)   
    return final_play,position

def can_moove (position:list,old_mouvement_grid):
    """
    check if the position the position we are going is on the mouvement_grid

    Args:
        position (list): position with the mouse on the grid
        old_mouvement_grid (list): the grid stocking the mouvement list

    Returns:
        bool : return true if we can go
    """    
    if mouvement_grid[position[0]][position[1]] == "Y":
        return True
    return False

def play(position, grid_of_the_game, selected_piece):
    """
    we moove the piece on the board

    Args:
        position (list): position of the mouse
        grid_of_the_game (list): the grid of the game
        selected_piece (list): the position of the piece we are moving

    Returns:
        list: the updated list
    """    
    which_piece = None
    #we are updating our list
    piece = grid_of_the_game[selected_piece[0]][selected_piece[1]]
    grid_of_the_game[position[0]][position[1]] = piece
    grid_of_the_game[selected_piece[0]][selected_piece[1]] = "--"
    #if the pawn is on the last line we can transform him in different piece
    if grid_of_the_game[position[0]][position[1]][1] == "P":
        if grid_of_the_game[position[0]][position[1]][0] == "W":
            if position[0] == 0: #if the piece is at the end of board we ask the player to know in what type of piece he want to transform the piece
                while which_piece !="Q" and which_piece !="T" and which_piece !="B" and which_piece != "N" : 
                    which_piece = str(input("en qu'elle piece veut tu transformer ton pion ? : \nEntre Q pour une dame\nEntre T pour une tour\nEntre N pour un cavalier\nEntre B pour un fou\n alors tu choisis quoi ? : "))
                piece = "W"+which_piece
                grid_of_the_game[position[0]][position[1]] = str(piece)
        else:
            if position[0] == 7:#if the piece is at the end of board we ask the player to know in what type of piece he want to transform the piece
                while which_piece !="Q" and which_piece !="T" and which_piece !="B" and which_piece != "N" : 
                    which_piece = str(input("en qu'elle piece veut tu transformer ton pion ? : \nEntre Q pour une dame\nEntre T pour une tour\nEntre N pour un cavalier\nEntre B pour un fou\n alors tu choisis quoi ? : "))
                piece = "B"+which_piece
                grid_of_the_game[position[0]][position[1]] = str(piece)
    
    return grid_of_the_game

def change_turn(turn:int):
    """
    changing the turn
    Args:
        turn (int): the turn value

    Returns:
        turn: the turn changed
    """    
    if turn == 1 :
        return 0
    else :
        return 1

def show_possibilty(grid:list,position:list,turn):
    """
    we are taking our grid,our position , and the turn to know where the piece which we click on can go 

    Args:
        grid (list): the grid of the game
        position (list): the position of the mouse
        turn (int): who's turn (white or black)

    Returns:
            list : a list who contain a grid of all the place the piece can go (Y are for "the piece can go there)
    """
    
    mouvement_grid = [
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],   
    ]
    #this "mouvement_grid" will be modifying she will contain all the place the piece can go
    plays,selected_piece = mouvement(grid,position,turn) #we need mouvement function which will give us all the position of the piece can go
    for play in plays :
        mouvement_grid[play[0]][play[1]] = "Y" #transforming empty slot into "Y"
    return selected_piece,mouvement_grid

def display_possibilty (mouvement_grid:list) :
    """
    this grid show the mouvement possible if you click on a piece

    Args:
        mouvement_grid (list): _description_
    """    
    axis_value = [0,75,150,225,300,375,450,525]
    color_value = 0 
    for y,line in enumerate(mouvement_grid) :
        for x,column in enumerate(line) :
            if  column == "Y":
                pygame.draw.rect(screen,"yellow",[axis_value[x],axis_value[y],75,75])
            if column == "R" :
                pygame.draw.rect(screen,"Red",[axis_value[x],axis_value[y],75,75])
            if column == "E" :
                pygame.draw.rect(screen,"yellow",[axis_value[x],axis_value[y],75,75])

def diagonale_right (position:list):
    """
    creating the diagonale →↓ for the mouvement function
    Args:
        position (list): the position 

    Returns:
        list: list of position which will be used for the mouvement function
    """    
    plays = []
    y = position[0]
    x = position[1]
    while x > 0 and y > 0 :
        x -= 1
        y -= 1
        plays.append([y,x])
    plays = list(reversed(plays)) # we are reversed because a wall can block us
    y = position[0]
    x = position[1]
    while x < 7 and y < 7 :
        x += 1
        y += 1
        plays.append([y,x])
    return plays

def diagonale_left (position:list) :
    """
    creating the diagonale →↑ for the mouvement func
    Args:
        position (list): the position 

    Returns:
        list: list of position which will be used for the mouvement function
    """    
    plays = []
    y = position[0]
    x = position[1]
    while x >= 0 and y < 7 :
        x -= 1
        y += 1
        plays.append([y,x])   #we are reversed because a wall can block us 
    plays = list(reversed(plays))
    y = position[0]
    x = position[1]
    while x < 7 and y > 0 :
        y -= 1
        x += 1
        plays.append([y,x])
    return plays

def there_is_a_check(position,grid,selected_piece,turn):
    """
    we are looking if the play there is a check situation
    Args:
        position (list): the position of piece moved
        grid (list): the grid
        selected_piece (list): the position of piece moved
        turn (int): the turn number

    Returns:
        bool: true if the piece is check , False if there is no check
    """    
    
    fake_grid = copy.deepcopy(grid) # we need the deepcopy function because we will modying the "fake_grid" but not the grid
    piece = grid[selected_piece[0]][selected_piece[1]] 
    fake_grid[position[0]][position[1]] = piece
    fake_grid[selected_piece[0]][selected_piece[1]] = "--"
    check_list = []
    random_piece = None
    check = None
    check,random_piece = check_for_a_check(fake_grid,turn) #importing the check_for_a_check function 
    return check,random_piece

def check_for_a_check(fake_grid,turn):
    """
    return true if the king is check
    Args:
        fake_grid (list): the list of the game
        turn (int): the turn

    Returns:
        bool: true if check ,False if not
    """    
    random_piece = None
    for line in range(len(fake_grid)):
            for piece in range(len(fake_grid[line])):
                if turn == 0 :
                    if fake_grid[line][piece][0] == "B": #if it's an enely piece
                        list_of_plays,random_piece = mouvement(fake_grid,[line,piece],1) #we are checking the position this piece can go
                        for plays in list_of_plays:
                            if fake_grid[plays[0]][plays[1]] == "WK": # if this piece can go on the position of the king that's mean it's check and then we are returning true
                                return True,random_piece
                else :
                    if fake_grid[line][piece][0] == "W": #if it's an enely piece
                        list_of_plays,random_piece = mouvement(fake_grid,[line,piece],0) #we are checking the position this piece can go
                        for plays in list_of_plays:
                            if fake_grid[plays[0]][plays[1]] == "BK": # if this piece can go on the position of the king that's mean it's check and then we are returning true
                                return True,random_piece
    return False,random_piece

def check_mate(turn,grid):
    """
    if there is a check mate True if yes , False if no, Pat if there is a pat
    to verify if there is a check we will :
    1: looking if in all the position of the king can go he will be check
    2: looking if an ally piece can't go between or on the piece who check the kink and the king
    Args:
        turn (list): the turn integral
        grid (list): the grid of the game

    Returns:
        bool or str: if there is a check mate True if yes , False if no, Pat if there is a pat
    """    
    where_king_can_go  = None
    position_to_go = []
    where_does_my_piece_can_go = []
    number = 0
    if turn == 1:
        for line in range(len(grid)):
            for piece in range(len(grid[line])):
                if grid[line][piece] == "WK": #if it's the king we are save his position
                    position = [line,piece]
                else:
                    if grid[line][piece][0] == "W": # else if it's an ally piece  
                        where_my_piece_can_go,random_piece = mouvement(grid,[line,piece],0)
                        where_does_my_piece_can_go.append((random_piece))
                        for mouvement_of_piece in where_my_piece_can_go:
                            check,random_piece = there_is_a_check(mouvement_of_piece,grid,[line,piece],0) # here we check if the mouvement is possible and doesn't go for a check 
                            if check == False:
                                where_does_my_piece_can_go.append(mouvement_of_piece) #save the position of this piece can go
                                number += 1 
        where_king_can_go,selected_piece = mouvement(grid,position,0) # also save the mouvement of the king
        for plays in where_king_can_go:
            check,random_piece = there_is_a_check(plays,grid,selected_piece,0) # we are trying to moove the king on every position and looking if it's check in this new position
            if check == False: #if not it's not a checkmate
                return False 
        check,position_of_the_piece_who_moove = check_for_a_check(grid,0)#we look if it's a check in this actual position (this will be used in the "pat" part) and returning the piece who is checking us
        # 1 :  first part is done 
        piece = grid[position_of_the_piece_who_moove[0]][position_of_the_piece_who_moove[1]] #we are looking about the piece who is actually check us
        if number != 0 : #if there is a piece who can moove
            if piece[1] == "T" or piece[1] == "Q": #if it's a rook or a queen
                if position_of_the_piece_who_moove[0] == position[0] : #if it's in same line
                    if position_of_the_piece_who_moove[1] < position[1] : #if the piece is before our king
                        difference = position[1]-position_of_the_piece_who_moove[1]-1 # we are creating a "difference" this difference will be a number and it's equal to the number of case between the kinf and the piece and the -1 is the number of the king could be
                        for value in range(0,difference):
                            position_to_go.append([position[0],position_of_the_piece_who_moove[1]+value]) # we are adding all the play of a piece could go to stop the check
                    else:
                        difference = position_of_the_piece_who_moove[1]-position[1] # if the piece who check us is after the king we are dojng the same 
                        for value in range(1,difference): # but this time we start at 1 because we don't want to add pur king
                            position_to_go.append([position[0],position[1]+value])
                elif position_of_the_piece_who_moove[1] == position[1]: #if the king and this piece are in the same row
                    if position_of_the_piece_who_moove[0] < position[0] : #if the piece is before
                        difference = position[0]-position_of_the_piece_who_moove[0] # we are doing the same strategy but for the column
                        for value in range(0,difference):
                            position_to_go.append([position_of_the_piece_who_moove[0]+value,position[1]])
                    else:
                        difference = position_of_the_piece_who_moove[0]-position[0]
                        for value in range(1,difference):
                            position_to_go.append([position[0]+value,position[1]])
            if piece[1] == "B" or piece[1] == "Q": #it it's a bishop or a queen
                if position[0]<position_of_the_piece_who_moove[0] : # here we are trying to know where is our bishop/queen for the king
                    if position[1]<position_of_the_piece_who_moove[1]:# here we are trying to know where is our bishop/queen for the king
                        difference = position_of_the_piece_who_moove[0]-position[0]+1 #then we do the same system again
                        for value in range(1,difference):
                            position_to_go.append([value+position[0],value+position[1]])
                    else :
                        difference = position_of_the_piece_who_moove[0]-position[0]+1 #then we do the same system again
                        for value in range(1,difference):
                            position_to_go.append([value+position[0],-value+position[1]])
                else :
                    if position[1]<position_of_the_piece_who_moove[1]:
                        difference = position[0]-position_of_the_piece_who_moove[0]+1#then we do the same system again
                        for value in range(1,difference):
                            position_to_go.append([-value+position[0],value+position[1]])
                    else :
                        difference = position[0]-position_of_the_piece_who_moove[0]+1#then we do the same system again
                        for value in range(1,difference):
                            position_to_go.append([-value+position[0],-value+position[1]])
            if piece[1] != "B" and piece[1] != "Q" and piece[1] != "T" :
                position_to_go.append([position_of_the_piece_who_moove[0],position_of_the_piece_who_moove[1]]) # otherwise we are adding only the position of the piece who check us
            for play in where_does_my_piece_can_go: 
                for go_here in position_to_go:
                    if play[0]-go_here[0] == 0 and play[1]-go_here[1] == 0 : # if there is a piece can go where it's needed to stop mate we return false
                        return False
        else : #if there is not possible play to do but the king is not checked
            if check == False :
                return("pat") #return pat
    else :
        check,random_piece = check_for_a_check(grid,1)
        for line in range(len(grid)):
            for piece in range(len(grid[line])):
                if grid[line][piece] == "BK": #if it's the king we are save his position
                    position = [line,piece]
                else:
                    if grid[line][piece][0] == "B": # else if it's an ally piece  
                        where_my_piece_can_go,random_piece = mouvement(grid,[line,piece],1)
                        where_does_my_piece_can_go.append((random_piece))
                        for mouvement_of_piece in where_my_piece_can_go:
                            check,random_piece = there_is_a_check(mouvement_of_piece,grid,[line,piece],1)
                            if check == False :
                                where_does_my_piece_can_go.append(mouvement_of_piece) #save the position of this piece can go
                                number += 1 
        where_king_can_go,selected_piece = mouvement(grid,position,1)
        for plays in where_king_can_go:
            check,randown_piece = there_is_a_check(plays,grid,selected_piece,1)
            if check == False:
                return False
        check,position_of_the_piece_who_moove = check_for_a_check(grid,1)
        piece = grid[position_of_the_piece_who_moove[0]][position_of_the_piece_who_moove[1]]
        if number != 0 : #if there is a piece who can moove
            if piece[1] == "T" or piece[1] == "Q": #if it's a rook or a queen
                if position_of_the_piece_who_moove[0] == position[0] : #if it's in same line
                    if position_of_the_piece_who_moove[1] < position[1] : #if the piece is before our king
                        difference = position[1]-position_of_the_piece_who_moove[1]-1 # we are creating a "difference" this difference will be a number and it's equal to the number of case between the kinf and the piece and the -1 is the number of the king could be
                        for value in range(0,difference):
                            position_to_go.append([position[0],position_of_the_piece_who_moove[1]+value]) # we are adding all the play of a piece could go to stop the check
                    else:
                        difference = position_of_the_piece_who_moove[1]-position[1] # if the piece who check us is after the king we are dojng the same 
                        for value in range(1,difference): # but this time we start at 1 because we don't want to add pur king
                            position_to_go.append([position[0],position[1]+value])
                elif position_of_the_piece_who_moove[1] == position[1]: #if the king and this piece are in the same row
                    if position_of_the_piece_who_moove[0] < position[0] : #if the piece is before
                        difference = position[0]-position_of_the_piece_who_moove[0] # we are doing the same strategy but for the column
                        for value in range(0,difference):
                            position_to_go.append([position_of_the_piece_who_moove[0]+value,position[1]])
                    else:
                        difference = position_of_the_piece_who_moove[0]-position[0]
                        for value in range(1,difference):
                            position_to_go.append([position[0]+value,position[1]])
            if piece[1] == "B" or piece[1] == "Q": #it it's a bishop or a queen
                if position[0]<position_of_the_piece_who_moove[0] : # here we are trying to know where is our bishop/queen for the king
                    if position[1]<position_of_the_piece_who_moove[1]:# here we are trying to know where is our bishop/queen for the king
                        difference = position_of_the_piece_who_moove[0]-position[0]+1 #then we do the same system again
                        for value in range(1,difference):
                            position_to_go.append([value+position[0],value+position[1]])
                    else :
                        difference = position_of_the_piece_who_moove[0]-position[0]+1 #then we do the same system again
                        for value in range(1,difference):
                            position_to_go.append([value+position[0],-value+position[1]])
                else :
                    if position[1]<position_of_the_piece_who_moove[1]:
                        difference = position[0]-position_of_the_piece_who_moove[0]+1#then we do the same system again
                        for value in range(1,difference):
                            position_to_go.append([-value+position[0],value+position[1]])
                    else :
                        difference = position[0]-position_of_the_piece_who_moove[0]+1#then we do the same system again
                        for value in range(1,difference):
                            position_to_go.append([-value+position[0],-value+position[1]])
            if piece[1] != "B" and piece[1] != "Q" and piece[1] != "T" :
                position_to_go.append([position_of_the_piece_who_moove[0],position_of_the_piece_who_moove[1]]) # otherwise we are adding only the position of the piece who check us
            for play in where_does_my_piece_can_go: 
                for go_here in position_to_go:
                    if play[0]-go_here[0] == 0 and play[1]-go_here[1] == 0 : # if there is a piece can go where it's needed to stop mate we return false
                        return False
        else :#if there is not possible play to do but the king is not checked
            if check == False :
                return("pat") # return pat 
    if check == False : # if the king is just not already checked return False
        return False
    
    return True # if after all the try there no clue it's checkmate return True

def tie(grid) :
    """
    look if the two team have enough piece to mate

    Args:
        grid (list): the grid of the game

    Returns:
        bool: true if it's tie false if not
    """    
    white_piece = []
    black_piece = []
    for line in grid :
        for piece in line :
            if piece[0] == "W":
                white_piece.append(piece) # if it's a white piece just add this piece to the white list
            elif piece[0] == "B":
                black_piece.append(piece)# if it's a black piece just add this piece to the black list
    if enough_piece(white_piece) and enough_piece(black_piece) : # if there not enought piece for the two team return True it's a tie
        return True 
    return False # otherwise no it's not a tie

def enough_piece(list:list) :
    """
    look if there is enough piece to mate with a given list
    
    Args:
        list (list): a list of pawn

    Returns:
        bool: False if it's still possible to mate True if not
    """    
    compteur = 0
    for element in list :
        if element[1] == "Q" or element[1] == "T" or element[1] =="P" : #if it's a tower , a queen or a pawn we can mate
            return False
        if element[1] == "B" or element[1] == "N":
            compteur +=1
    if compteur > 1: #if there more than one knight and bishop we can mate 
        return False
    return True

def print_the_rock(grid,turn,king_pos,king_next_pos,tower_pos,tower_next_pos):
    """
    do the same than the normal game loop but applies a rock who need special treatement

    Args:
        grid (list): the grid of the game
        turn (int): the number for the turn
        king_pos (list): the pos of the king
        king_next_pos (list): the pos of the king after the rock
        tower_pos (list): the pos of the tower
        tower_next_pos (list): he pos of the tower after the rock 

    Returns:
        bool: true if we do the play False if not
        int : thr turn chanhed
    """    
    statement = False
    global game,selected_piece,mouvement_grid
    
    fake_grid = copy.deepcopy(grid)
    piece = fake_grid[king_pos[0]][king_pos[1]]
    fake_grid[king_next_pos[0]][king_next_pos[1]] = piece
    fake_grid[king_pos[0]][king_pos[1]] = "--"
    piece = fake_grid[tower_pos[0]][tower_pos[1]]
    fake_grid[tower_next_pos[0]][tower_next_pos[1]] = piece
    fake_grid[tower_pos[0]][tower_pos[1]] = "--"
    check,random_piece = check_for_a_check(fake_grid,turn) # we verify if after the rook there is no check
    
    if check== False:
        statement = True # we do the rock so statement to True
        grid = play(king_next_pos,grid,king_pos) #moove the king
        grid = play(tower_next_pos,grid,tower_pos) #moove the rock
        mate = check_mate(turn,grid) # look for a possible mate
        if mate == True:
            game = False #chnaged game statement if yes
        if mate == ("pat") : # look for a pat
            game = False
            print("Il y a pat :)")
        if tie(grid) : #look for a tie
            game = False
            print("Il y a egalité par manque de materiel :)")
        turn = change_turn(turn) # changed the turn
        selected_piece = None # reinitialize a variable
        mouvement_grid = [["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"]]
    return statement,turn

    def choose_where_rock(grid,turn,position) :
        """
        choose what rock do

        Args:
            grid (list): list of the game
            turn (int): who's turn
            position (list): the pos of the mouse on the grid

        Returns:
            bool: true if we do the rock
            int : the turn
        """        
    statement = False
    if turn == 0:  # if it's white's turn
        if position[1] == 0 :  # if the mouse is on the left tower: set the correct variable and then run the function
            king_pos = [7,4] 
            king_next_pos = [7,2]
            tower_pos = position
            tower_next_pos = [7,3]
            statement,turn = print_the_rock(grid,turn,king_pos,king_next_pos,tower_pos,tower_next_pos)
            return statement,turn
        if position[1] == 7 : # if the mouse is on the right tower: set the correct variable and then run the function
            king_pos = [7,4]
            king_next_pos = [7,6]
            tower_pos = position
            tower_next_pos = [7,5]
            statement,turn = print_the_rock(grid,turn,king_pos,king_next_pos,tower_pos,tower_next_pos)
            return statement,turn
    if turn == 1: # if it's black's turn
        if position[1] == 0 : # if the mouse is on the left tower: set the correct variable and then run the function
            king_pos = [0,4]
            king_next_pos = [0,2]
            tower_pos = position
            tower_next_pos = [0,3]
            statement,turn = print_the_rock(grid,turn,king_pos,king_next_pos,tower_pos,tower_next_pos)
            return statement,turn
        if position[1] == 7 : # if the mouse is on the right tower: set the correct variable and then run the function
            king_pos = [0,4]
            king_next_pos = [0,6]
            tower_pos = position
            tower_next_pos = [0,5]
            statement,turn = print_the_rock(grid,turn,king_pos,king_next_pos,tower_pos,tower_next_pos)
            return statement,turn
    return statement,turn

def try_en_passant(position,grid,selected_piece,turn,pos_of_en_passant):
    """
    apply the "possible en passant" and look if there is a check

    Args:
        position (list): the pos of the mouse
        grid (list): the grid of the game
        selected_piece (list): the pice selected
        turn (int): the turn value
        pos_of_en_passant (list)): the pos of the who will be en passant

    Returns:
        _type_: _description_
    """    
    
    fake_grid = copy.deepcopy(grid) 
    piece = grid[selected_piece[0]][selected_piece[1]]
    fake_grid[position[0]][position[1]] = piece
    fake_grid[selected_piece[0]][selected_piece[1]] = "--"
    fake_grid[pos_of_en_passant[0]][pos_of_en_passant[1]] = "--"
    # we modify the grid with corred value
    check,random_piece = check_for_a_check(fake_grid,turn) # look if there is check 
    return check # return  the check value

def apply_en_passant(grid,position,pos_of_en_passant,selected_piece) :
    """
    we do the en passant on the grid

    Args:
        grid (list): the grid of the game
        position (list): the pos of the mouse ( in our case the position of the pawn will go)
        pos_of_en_passant (list): position of the pawn who will be destroy after the en passant
        selected_piece (list): the pawn who moved

    Returns:
        
    """    
    global en_passant,game,turn,mouvement_grid
    piece = grid[selected_piece[0]][selected_piece[1]]
    grid[position[0]][position[1]] = piece
    grid[selected_piece[0]][selected_piece[1]] = "--"
    grid[pos_of_en_passant[0]][pos_of_en_passant[1]] = "--"
    # modify the grid
    en_passant = False  # set the value of a possible en passant to false
    mate = check_mate(turn,grid) #look for a mate
    if mate == True:  #if mate change the game statement
        game = False
    if mate == ("pat") : #if it's a pat change the game statement
        game = False
        print("Il y a pat :)")
    turn = change_turn(turn) #change the turn
    selected_piece = None # reset the value
    mouvement_grid = [["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"]]
    return 

def en_passant_mouvement(mouvement_grid,position,pos_of_en_passant,turn):
    """
    modify the mouvement grid for an en passant

    Args:
        mouvement_grid (list): list of all the possible mouvement
        position (list): the actual position
        pos_of_en_passant (list): the pos of the piece who moove 2 square last play
        turn (int): the turn value
    """    
    if turn == 0 :  # if it's white's turn
        mouvement_grid[position[0]-1][pos_of_en_passant[1]] = "E" #modify the mouvement grid 
    else : # if it's black's turn
        mouvement_grid[position[0]+1][pos_of_en_passant[1]] = "E" #modify the mouvement grid
    return 

pygame.init() #initalize pygame 
screen = pygame.display.set_mode((600,600)) # set the size of the window
pygame.display.set_caption("echec") # set the name 

#set the variable for a normal game
grid = [  # set the grid to the correct start position
    ["BT","BN","BB","BQ","BK","BB","BN","BT"],
    ["BP","BP","BP","BP","BP","BP","BP","BP"],
    ["--","--","--","--","--","--","--","--"], 
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["WP","WP","WP","WP","WP","WP","WP","WP"],
    ["WT","WN","WB","WQ","WK","WB","WN","WT"]
    ]
mouvement_grid = [ # set the grid to the correct start position
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"]
    ]
black_left_tower_moove_counter = 0
black_right_tower_moove_counter = 0
white_left_tower_moove_counter = 0
white_right_tower_moove_counter = 0
white_king_moove_counter = 1
black_king_moove_counter = 1
turn = 0
game = True
en_passant = False
pos_of_en_passant = [0,0]



#importing and scale all the piece
#white 
white_king_sprite = pygame.image.load("piece\\roi_blanc.png").convert_alpha()
white_king_sprite = pygame.transform.scale(white_king_sprite,(60,60))

white_queen_sprite = pygame.image.load("piece\\dame_blanc.png").convert_alpha()
white_queen_sprite = pygame.transform.scale(white_queen_sprite,(60,60))

white_tower_sprite = pygame.image.load("piece\\tour_blanc.png").convert_alpha()
white_tower_sprite = pygame.transform.scale(white_tower_sprite,(60,60))

white_knight_sprite = pygame.image.load("piece\\cavalier_blanc.png").convert_alpha()
white_knight_sprite = pygame.transform.scale(white_knight_sprite,(60,60))

white_bishop_sprite = pygame.image.load("piece\\fou_blanc.png").convert_alpha()
white_bishop_sprite = pygame.transform.scale(white_bishop_sprite,(60,60))

white_pawn_sprite = pygame.image.load("piece\\pion_blanc.png").convert_alpha()
white_pawn_sprite = pygame.transform.scale(white_pawn_sprite,(60,60))

#black
black_king_sprite = pygame.image.load("piece\\roi_noir.png").convert_alpha()
black_king_sprite = pygame.transform.scale(black_king_sprite,(60,60))

black_queen_sprite = pygame.image.load("piece\\dame_noir.png").convert_alpha()
black_queen_sprite = pygame.transform.scale(black_queen_sprite,(60,60))

black_tower_sprite = pygame.image.load("piece\\tour_noir.png").convert_alpha()
black_tower_sprite = pygame.transform.scale(black_tower_sprite,(60,60))

black_knight_sprite = pygame.image.load("piece\\cavalier_noir.png").convert_alpha()
black_knight_sprite = pygame.transform.scale(black_knight_sprite,(60,60))

black_bishop_sprite = pygame.image.load("piece\\fou_noir.png").convert_alpha()
black_bishop_sprite = pygame.transform.scale(black_bishop_sprite,(60,60))

black_pawn_sprite = pygame.image.load("piece\\pion_noir.png").convert_alpha()
black_pawn_sprite = pygame.transform.scale(black_pawn_sprite,(60,60))


while True :
    if game : #if the game mode is on True
        print_board() # print the board(only the squares)
        display_possibilty(mouvement_grid) # print the square of the mouvement grid
        print_piece(grid) #print the piece
        for event in pygame.event.get():
                if event.type == pygame.QUIT: # if the user quit the game end it
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN : # if the player click
                    position = where_am_i(pygame.mouse.get_pos()) # we know where on the grid the player click
                    if can_moove(position,mouvement_grid) : #if there is play on the mouvement grid
                        check,position_of_a_piece = there_is_a_check(position,grid,selected_piece,turn) # look if this moove give a check
                        if check == False: #if not we can play it
                            grid = play(position,grid,selected_piece) #modify the grid
                            if grid[position[0]][position[1]][1]  == "P": #if it was a pawn who mooved
                                difference = position[0]-selected_piece[0] 
                                if difference == 2 or difference == -2 : #if it moove 2 square
                                    en_passant,pos_of_en_passant = True,position 
                                else :
                                    en_passant = False
                            else :
                                en_passant = False

                            mate = check_mate(turn,grid) # look for a mate
                            if mate == True: #if it's one 
                                game = False  # set the game mode to false
                            if mate == ("pat") : # if it's a pat
                                game = False  # set the game mode to false
                                print("Il y a pat :)")
                            if tie(grid) : #if it's a tie
                                game = False # set the game mode to false
                                print("Il y a egalité par manque de materiel :)")
                            turn = change_turn(turn)  #change the turn
                            selected_piece = None # redifine so variable
                            mouvement_grid = [["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"]]
                            
                            if turn == 0 : #if it was black's turn 
                                if grid[position[0]][position[1]] == "BK" : #if the piece who moove was the black king
                                    black_king_moove_counter += 1 #this value is used for the rock system
                                elif grid[position[0]][position[1]] == "BT" : #if the piece who moove was a black tower
                                    if position[1] == 0: # if it was the left one
                                        black_left_tower_moove_counter += 1  #this value is used for the rock system
                                    if position[1] == 6 : # if it was the right one
                                        black_right_tower_moove_counter += 1#this value is used for the rock system
                            if turn == 1 :#if it was white's turn 
                                if grid[position[0]][position[1]] == "WK" :#if the piece who moove was the white king
                                    white_king_moove_counter += 1#this value is used for the rock system
                                elif grid[position[0]][position[1]] == "WT" :#if the piece who moove was the white tower
                                    if position[1] == 0: # if it was the left one
                                        white_left_tower_moove_counter += 1#this value is used for the rock system
                                    if position[1] == 6 : # if it was the right one
                                        white_right_tower_moove_counter += 1#this value is used for the rock system
                                        
                    elif mouvement_grid[position[0]][position[1]] == "R": # if we mooved for a rock
                        check,random_piece = check_for_a_check(grid,turn) #look if we can rock
                        if check == False:
                            rock_statement,turn = choose_where_rock(grid,turn,position) #do the play
                            if rock_statement :
                                if turn == 0 :
                                    black_king_moove_counter += 1 #this value is used for the rock system
                                if turn == 1 :
                                    white_king_moove_counter += 1 #this value is used for the rock system
                                    
                    elif mouvement_grid[position[0]][position[1]] == "E": # if we mooved for a en passant
                        check = try_en_passant(position,grid,selected_piece,turn,pos_of_en_passant)  #look if we can en passant
                        if check == False :
                            grid = apply_en_passant(grid,position,pos_of_en_passant,selected_piece)  #do the en passant
                            
                    else : # if the play is not on the mouvement grid
                        selected_piece,mouvement_grid = show_possibilty(grid,position,turn) # set the new mouvement grid depending on what you click on
                        if grid[selected_piece[0]][selected_piece[1]][1] == "P" : # if it's a pawn
                            if en_passant: #if the en passant value is true
                                difference_x = pos_of_en_passant[1]-selected_piece[1]
                                if difference_x == 1 or difference_x == -1: #if the en passant column is next to the columb of the piece
                                    if selected_piece[0] == pos_of_en_passant[0] : #if we those piece are on the same row
                                        mouvement_grid = en_passant_mouvement(mouvement_grid,position,pos_of_en_passant,turn) # modify the mouvement grid
                                        
                        if turn == 0 : #if it's white's turn
                            if grid[selected_piece[0]][selected_piece[1]] == "WK": #if we click on the white king
                                if white_king_moove_counter == 0 : #if this king doesn't moove before
                                    if white_right_tower_moove_counter == 0 :# if the tower doesn't moove to
                                        if grid[7][1] == "--" and grid[7][2] == "--" and grid[7][3] == "--":#if the space between the king and the tower is empty
                                            mouvement_grid[7][0] = "R" # we add the rock on the mouvement grid
                                    if white_left_tower_moove_counter == 0 :# if the tower doesn't moove to
                                        if grid[7][5] == "--" and grid[7][6] == "--":#if the space between the king and the tower is empty
                                            mouvement_grid[7][7] = "R"# we add the rock on the mouvement grid
                        else : #if it's black's turn
                            if grid[selected_piece[0]][selected_piece[1]] == "BK":#if we click on the black king
                                if black_king_moove_counter == 0 : #if this king doesn't moove before
                                    if black_right_tower_moove_counter == 0 : # if the tower doesn't moove to
                                        if grid[0][1] == "--" and grid[0][2] == "--" and grid[0][3] == "--": #if the space between the king and the tower is empty
                                            mouvement_grid[0][0] = "R"# we add the rock on the mouvement grid
                                    if black_left_tower_moove_counter == 0 :# if the tower doesn't moove to
                                        if grid[0][5] == "--" and grid[0][6] == "--":#if the space between the king and the tower is empty
                                            mouvement_grid[0][7] = "R"# we add the rock on the mouvement grid
    
    else : #if the game statement is false
        for event in pygame.event.get(): #if the player want to quit we close the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN: # if he press any keys we reinitialyse the value for a new game
                    black_left_tower_moove_counter = 0
                    black_right_tower_moove_counter = 0
                    white_left_tower_moove_counter = 0
                    white_right_tower_moove_counter = 0
                    white_king_moove_counter = 0
                    black_king_moove_counter = 0
                    turn = 0
                    game = True
                    grid = [
                        ["BT","BN","BB","BQ","BK","BB","BN","BT"],
                        ["BP","BP","BP","BP","BP","BP","BP","BP"],
                        ["--","--","--","--","--","--","--","--"],
                        ["--","--","--","--","--","--","--","--"],
                        ["--","--","--","--","--","--","--","--"],
                        ["--","--","--","--","--","--","--","--"],
                        ["WP","WP","WP","WP","WP","WP","WP","WP"],
                        ["WT","WN","WB","WQ","WK","WB","WN","WT"]
                        ]
        print_board() # print the board
        print_piece(grid) #print the piece
        
    pygame.display.flip() # we actualize the screen with all the modification
    