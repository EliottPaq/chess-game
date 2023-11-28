import pygame
from piece import *
import copy

def print_board () :
    """
    this function just prints the board (white and black square)
    """    
    
    axis_value = [0,75,150,225,300,375,450,525] #those value are the limit of each square in x and y axis
    color_value = 0 #this value is needed to set a variable color
    for y in axis_value :
        for x in axis_value :
            if color_value == 0 :
                pygame.draw.rect(screen,"white",[x,y,75,75]) #75,75 is the height and length of each square
                if x != 525 :# at the last rectangle, we are not changing the color because otherwise, it will be a real chessboard
                    color_value = 1
            elif color_value== 1 :
                pygame.draw.rect(screen,"black",[x,y,75,75]) #75,75 is the height and length of each square
                if x != 525:
                    color_value = 0# at the last rectangle we are not changing the color because otherwise it wouldn't be a real chessboard

def where_am_i (mouse_pos:list):
    """
    we are transforming the mouse_pos in a place in our grid that is readable

    Args:
        mouse_pos (list): our mouse position [x,y]

    Returns:
        list: the position of our mouse in the grid [y,x]
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

def print_piece (grid: list) :
    """
    this function adds the piece to the board
    Args:
        grid (list): it's the list that contains all our piece
    """    
    
    axis_value = [0,75,150,225,300,375,450,525] #those value are the limit of each square in x and y axis
    for row in grid:
        for piece in row :
            if piece != None:
                piece_surf = piece.sprite.get_rect(center = (axis_value[piece.position[1]]+37.5,axis_value[piece.position[0]]+37.5)) # 37.5 is half of 75 by using this value we are placing our piece in the middle of each square
                screen.blit(piece.sprite,piece_surf)

def display_possibility (movement_list:list) :
    """
    this grid shows the movement possible if you click on a piece

    Args:
        movement_list (list): _description_
    """    
    axis_value = [0,75,150,225,300,375,450,525]
    for move in movement_list :
        pygame.draw.rect(screen,"yellow",[axis_value[move[1]],axis_value[move[0]],75,75])

def screen_update(board:list,movement_list:list):
    """
    this function is actualizing the screen by calling all the "visual" function
    Args:
        board (list): our board
        movement_list (list): a list of moves possible
    """
    print_board() #print the black and white board
    display_possibility(movement_list) #print all the move possible
    print_piece(board)  #print the piece
    pygame.display.flip() # We actualize the screen with all the modification

def move_piece(piece:object,board:list,position:list,list_of_move:list) :
    """
    move the piece 
    Args:
        piece (object): the piece we are moving
        board (list): the current board
        position (list): the future position of the piece
        list_of_move (list): the list who stocks all the move
    """
    if board[position[0]][position[1]] != None : #if we aren't moving to an empty squares
        if board[position[0]][position[1]].color == piece.color: #if the piece is going to be a piece of the same color it can only be a rock
            if piece.color == "B" :
                if piece.position ==[0,0]:
                    board[0][3] = piece
                    board[0][3].position = [0,3]
                    board[0][2] = board[0][4]
                    board[0][2].position = [0,2]
                elif piece.position == [0,7] :
                    board[0][5] = piece
                    board[0][5].position = [0,5]
                    board[0][6] = board[0][4]
                    board[0][6].position = [0,6]
            else:
                if piece.position == [7,0] :
                    board[7][3] = piece
                    board[7][3].position = [7,3]
                    board[7][2] = board[7][4]
                    board[7][2].position = [7,2]
                elif piece.position == [7,7] :
                    board[7][5] = piece
                    board[7][5].position = [7,5]
                    board[7][6] = board[7][4]
                    board[7][6].position = [7,6]
            movement_soud.play()
        else : 
            board[position[0]][position[1]] = piece
            board[piece.position[0]][piece.position[1]] = None
            board[position[0]][position[1]].position = position
            capture_soud.play()
    else :
        movement_soud.play()
        if piece.name == "P" and (position[1]-1 == piece.position[1] or position[1]+1 == piece.position[1]): #if the piece is doing on an "en passant"
            if piece.color == "W":
                board[position[0]+1][position[1]] = None #delete the piece that is getting captured by the "en passant"
            else:
                board[position[0]-1][position[1]] = None #delete the piece that is getting captured by the "en passant"
        board[position[0]][position[1]] = piece
        board[piece.position[0]][piece.position[1]] = None
        board[position[0]][position[1]].position = position
    if piece.name == "P" and position[0] == 0 : #if the pawn is at the opposite side we are changing it into queen
        movement_soud.play()
        board[position[0]][position[1]] = Queen("W",position,"piece\\dame_blanc.png")
    elif piece.name == "P" and position[0] == 7 :#if the pawn is at the opposite side we are changing it into queen
        movement_soud.play()
        board[position[0]][position[1]] = Queen("W",position,"piece\\dame_noir.png")

    board[position[0]][position[1]].move_counter +=1 
    list_of_move.append([piece.name,position])

def update_movement ( board: list,turn:str,list_of_move: list) -> None :
    """
    update the movement of all the piece
    Args:
        board (list): the board
        turn (str): who's turn
        list_of_move (list): list of all the plays
    """
    for line in board :
        for piece in line :
            if piece != None :
                piece.move(board,turn,list_of_move)

def clone_board (board:list,second_board:list)-> None :
    """
    copy the first board to the second

    Args:
        board (list): a current grid we want to copy
        second_board (list): the grid that is getting copied on
    """
    
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == None:  #if the square is empty we are chaning to None
                second_board[y][x] = None
            elif board[y][x] != None and board[y][x].name == "P": #if it's a piece we are recreating this object because just "copy" it would just copy "the pointer" instead of the object 
                second_board[y][x] = Pawn(board[y][x].color, board[y][x].position, board[y][x].sprite_pathing, board[y][x].move_counter) #calling the object with the current parameters
            elif board[y][x] != None and board[y][x].name == "K" :
                second_board[y][x] = King(board[y][x].color, board[y][x].position,board[y][x].sprite_pathing,board[y][x].move_counter)
            elif board[y][x] != None and board[y][x].name ==  "R" :
                second_board[y][x] = Rook(board[y][x].color, board[y][x].position,board[y][x].sprite_pathing,board[y][x].move_counter)
            elif board[y][x] != None and board[y][x].name == "Q" :
                second_board[y][x] = Queen(board[y][x].color,board[y][x].position,board[y][x].sprite_pathing,board[y][x].move_counter)
            elif board[y][x] != None and board[y][x].name == "B" :
                second_board[y][x] = Bishop(board[y][x].color,board[y][x].position,board[y][x].sprite_pathing,board[y][x].move_counter)
            elif board[y][x] != None and board[y][x].name == "N" :
                second_board[y][x] = Knight(board[y][x].color,board[y][x].position,board[y][x].sprite_pathing,board[y][x].move_counter)
    
def check(position:list,board:list,piece_selected:object,turn:str,list_of_move:list)->bool:
    """
    return True if there is no check with the move we are planning to do
    Args:
        position (list): where we want the piece to go
        board (list): the board
        piece_selected (object): the piece we are moving
        turn (str): who's turn
        list_of_move (list): a list of all the move

    Returns:
        bool: the bool to know if there is no check with the move we are planning to do
    """

    move_piece(piece_selected,board,position,list_of_move) # doing the move
    return not verify_check(board,turn) # return the

def verify_check(board:list,turn:str)->bool:
    """
    return True if there is a check, False if there is no check
    Args:
        board (list): the board we are analyzing
        turn (str): who's turn

    Returns:
        Bool: the check bool
    """
    if turn == "W" : #if the turn is white we want to know if a black piece can eat the king
        update_movement(board,"B",list_of_move)
        for line in board :
            for piece in line:
                if piece != None:
                    if piece.color == "B" :
                        for move_of_piece in piece.movement_list:
                            if board[move_of_piece[0]][move_of_piece[1]] != None and board[move_of_piece[0]][move_of_piece[1]].name == "K" and board[move_of_piece[0]][move_of_piece[1]].color == "W" :
                                return True
    else:
        update_movement(board,"W",list_of_move)
        for line in board :
            for piece in line:
                if piece != None:
                    if piece.color == "W":
                        for move_of_piece in piece.movement_list:
                            if board[move_of_piece[0]][move_of_piece[1]] != None and board[move_of_piece[0]][move_of_piece[1]].name == "K" and board[move_of_piece[0]][move_of_piece[1]].color == "B" :
                                return True
    return False #if the program goes to this it means no piece can eat the king so there is no check

def checkmate (board:list,second_board:list,turn:str,list_of_move:list)->bool:
    """
        return True if there is a checkmate False otherwise
        
        A checkmate respects two conditions:-the king can't go anwere without being eaten 
                                           -no piece can go between or on the piece who check and the king
                                           -if the king can't go anywere without being eaten and there 2 pieces or more checking him it's a checkmate
    Args:
        board (list): the board
        second_board (list): a second board that is a copy of the first one
        turn (str): who's turn
        list_of_move (list): the list of all the move

    Returns:
        bool: the checkmate bool
    """
    piece_who_check = [] #stocking all the piece who gives a check on the king
    good_color_piece = [] #stocking all the pieces who could stop the check
    if turn == "W":
        if verify_check(board,"B"): #if there is a check on the current grid
            for y in range(len(board)):
                for x in range(len(board[y])):
                    if board[y][x] != None:
                        if board[y][x].name == "K" and board[y][x].color == "B" : # if the piece is the king we are looking for
                            for move in board[y][x].movement_list:
                                if check(move,board,board[y][x],"B",list_of_move): # if the king can escape somewhere without being eaten it's not a checkmate
                                    list_of_move.pop(-1) #deleting the last element because in the call of "check", we are adding the move we are trying
                                    clone_board(second_board,board) #reseting the board
                                    return False
                                list_of_move.pop(-1)
                                clone_board(second_board,board)
                        if board[y][x].color == "W": # if the piece is in the "enemy" team of the king
                            for move in board[y][x].movement_list:
                                if board[move[0]][move[1]] != None:
                                    if board[move[0]][move[1]].name == "K" and board[move[0]][move[1]].color == "B" :
                                        piece_who_check.append(board[y][x]) # If the can be eaten by this we add it to the correct list
                        else:
                            good_color_piece.append(board[y][x]) #if the piece is on the same team as the king we add it to the list of all the pieces who could stop the checkmate
            if len(piece_who_check) > 1 : #if the king has nowhere to go and there is more than one piece checking him it's checkmate
                return True
            else:
                for piece in good_color_piece:
                    for move_can_do in piece.movement_list : #for all the moves of all the friendly piece
                        if check(move_can_do,board,piece,"B",list_of_move): #if after the move of the piece, it's not a check then it's not a checkmate
                            list_of_move.pop(-1)
                            clone_board(second_board,board)
                            return False
                        list_of_move.pop(-1)
                        clone_board(second_board,board)
        else:
            return False # if it's not a check then it's not a checkmate
    else: #applying the same logic but to the white piece
        if verify_check(board,"W"):
            for y in range(len(board)):
                for x in range(len(board[y])):
                    if board[y][x] != None:
                        if board[y][x].name == "K" and board[y][x].color == "W" :
                            for move in board[y][x].movement_list:
                                if check(move,board,board[y][x],"W",list_of_move):
                                    list_of_move.pop(-1)
                                    clone_board(second_board,board)
                                    return False
                                list_of_move.pop(-1)
                                clone_board(second_board,board)
                        if board[y][x].color == "B":
                            for move in board[y][x].movement_list:
                                if board[move[0]][move[1]] != None:
                                    if board[move[0]][move[1]].name == "K" and board[move[0]][move[1]].color == "W" :
                                        piece_who_check.append(board[y][x])
                        else:
                            good_color_piece.append(board[y][x])
            if len(piece_who_check) > 1 : 
                return True
            else:
                for piece in good_color_piece:
                    for move_can_do in piece.movement_list :
                        if check(move_can_do,board,piece,"W",list_of_move):
                            list_of_move.pop(-1)
                            clone_board(second_board,board)
                            return False
                        list_of_move.pop(-1)
                        clone_board(second_board,board)
        else:
            return False
    return True

def equality_verificator(board:list,turn:str,second_grid:list,list_of_play:list)->bool:
    pat(board,turn,second_grid,list_of_play)
    no_piece_to_mate(board)

def pat(board:list,turn:str,second_board:list,list_of_move:list)->bool:
    """
        pat is when no piece can move :
    Args:
        board (list): the board
        turn (str): who's turn
        second_board (list): a copy of the board
        list_of_move (list): the list of all the move

    Returns:
        bool: the pat's bool
    """
    for line in board:
        for piece in line:
            if piece != None :
                if piece.color != turn : # if the piece of the next team
                    for move in piece.movement_list :
                        if check(move,board,piece,"B",list_of_move): # If we can go somewhere without getting a check then it's not a pat
                            list_of_move.pop(-1) #deleting the last element because in the call of "check" we are adding the move we are trying
                            clone_board(second_board,board) #reseting the board
                            return False
                        list_of_move.pop(-1)
                        clone_board(second_board,board)
    return True

def no_piece_to_mate(board:list)->bool:
    """
    the null by not having enough pieces is when we have the current situation: king vs king or minor piece + king vs king
    Args:
        board (list): the board

    Returns:
        bool:  bool
    """
    piece_score = 0
    for line in board:
        for piece in line:
            if piece != None:
                if piece.name =="R" or piece.name == "Q" or piece.name == "P":
                    return False
                elif piece.name == "N" or piece.name == "B":
                    piece_score += 1
    if piece_score >= 2: 
        return False
    return True


pygame.init() #initalize pygame 
screen = pygame.display.set_mode((600,600)) # set the size of the window
pygame.display.set_caption("echec") # set the name 
capture_soud = pygame.mixer.Sound("sound\\capture.mp3")
movement_soud = pygame.mixer.Sound("sound\\move-self.mp3")

board = [ # set the grid to the correct start position
        [Rook("B",[0,0],"piece\\tour_noir.png",0),Knight("B",[0,1],"piece\\cavalier_noir.png",0),Bishop("B",[0,2],"piece\\fou_noir.png",0),Queen("B",[0,3],"piece\\dame_noir.png",0),King("B",[0,4],"piece\\roi_noir.png",0),Bishop("B",[0,5],"piece\\fou_noir.png",0),Knight("B",[0,6],"piece\\cavalier_noir.png",0),Rook("B",[0,7],"piece\\tour_noir.png",0)],
        [Pawn("B",[1,0],"piece\\pion_noir.png",0),Pawn("B",[1,1],"piece\\pion_noir.png",0),Pawn("B",[1,2],"piece\\pion_noir.png",0),Pawn("B",[1,3],"piece\\pion_noir.png",0),Pawn("B",[1,4],"piece\\pion_noir.png",0),Pawn("B",[1,5],"piece\\pion_noir.png",0),Pawn("B",[1,6],"piece\\pion_noir.png",0),Pawn("B",[1,7],"piece\\pion_noir.png",0)],
        [None,None,None,None,None,None,None,None], 
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [Pawn("W",[6,0],"piece\\pion_blanc.png",0),Pawn("W",[6,1],"piece\\pion_blanc.png",0),Pawn("W",[6,2],"piece\\pion_blanc.png",0),Pawn("W",[6,3],"piece\\pion_blanc.png",0),Pawn("W",[6,4],"piece\\pion_blanc.png",0),Pawn("W",[6,5],"piece\\pion_blanc.png",0),Pawn("W",[6,6],"piece\\pion_blanc.png",0),Pawn("W",[6,7],"piece\\pion_blanc.png",0)],
        [Rook("W",[7,0],"piece\\tour_blanc.png",0),Knight("W",[7,1],"piece\\cavalier_blanc.png",0),Bishop("W",[7,2],"piece\\fou_blanc.png",0),Queen("W",[7,3],"piece\\dame_blanc.png",0),King("W",[7,4],"piece\\roi_blanc.png",0),Bishop("W",[7,5],"piece\\fou_blanc.png",0),Knight("W",[7,6],"piece\\cavalier_blanc.png",0),Rook("W",[7,7],"piece\\tour_blanc.png",0)]
        ]
second_board = [ # set the grid to the correct start position
        [Rook("B",[0,0],"piece\\tour_noir.png",0),Knight("B",[0,1],"piece\\cavalier_noir.png",0),Bishop("B",[0,2],"piece\\fou_noir.png",0),Queen("B",[0,3],"piece\\dame_noir.png",0),King("B",[0,4],"piece\\roi_noir.png",0),Bishop("B",[0,5],"piece\\fou_noir.png",0),Knight("B",[0,6],"piece\\cavalier_noir.png",0),Rook("B",[0,7],"piece\\tour_noir.png",0)],
        [Pawn("B",[1,0],"piece\\pion_noir.png",0),Pawn("B",[1,1],"piece\\pion_noir.png",0),Pawn("B",[1,2],"piece\\pion_noir.png",0),Pawn("B",[1,3],"piece\\pion_noir.png",0),Pawn("B",[1,4],"piece\\pion_noir.png",0),Pawn("B",[1,5],"piece\\pion_noir.png",0),Pawn("B",[1,6],"piece\\pion_noir.png",0),Pawn("B",[1,7],"piece\\pion_noir.png",0)],
        [None,None,None,None,None,None,None,None], 
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [Pawn("W",[6,0],"piece\\pion_blanc.png",0),Pawn("W",[6,1],"piece\\pion_blanc.png",0),Pawn("W",[6,2],"piece\\pion_blanc.png",0),Pawn("W",[6,3],"piece\\pion_blanc.png",0),Pawn("W",[6,4],"piece\\pion_blanc.png",0),Pawn("W",[6,5],"piece\\pion_blanc.png",0),Pawn("W",[6,6],"piece\\pion_blanc.png",0),Pawn("W",[6,7],"piece\\pion_blanc.png",0)],
        [Rook("W",[7,0],"piece\\tour_blanc.png",0),Knight("W",[7,1],"piece\\cavalier_blanc.png",0),Bishop("W",[7,2],"piece\\fou_blanc.png",0),Queen("W",[7,3],"piece\\dame_blanc.png",0),King("W",[7,4],"piece\\roi_blanc.png",0),Bishop("W",[7,5],"piece\\fou_blanc.png",0),Knight("W",[7,6],"piece\\cavalier_blanc.png",0),Rook("W",[7,7],"piece\\tour_blanc.png",0)]
        ]

turn = "W"
print_board()
update_movement(board,turn,[])
print_piece(board)
pygame.display.flip() # We actualize the screen with all the modification
list_of_move = []
piece_selected = None
have_move = False
game_end = False

while True : 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If the user quits the game end it
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN :
            if game_end == False :
                position = where_am_i(pygame.mouse.get_pos())  # we know where on the grid the player click
                piece = board[position[0]][position[1]]
                if piece_selected != None :
                    if piece_selected.color == turn :
                        for move in piece_selected.movement_list:
                            if move ==  position :
                                if check(position,board,piece_selected,turn,list_of_move) :
                                    clone_board(board,second_board)
                                    if checkmate(board,second_board,turn,list_of_move)or equality_verificator(board,turn):
                                        screen_update(board,[])
                                        game_end=True
                                        break
                                    if turn == "W" : 
                                        turn = "B"
                                    else : 
                                        turn = "W"
                                    update_movement(board,turn,list_of_move)
                                    screen_update(board,[])
                                    piece_selected = None
                                    have_move = True
                                    break
                                else:
                                    clone_board(second_board,board)
                                    update_movement(board,turn,list_of_move)
                                    screen_update(board,[])
                                    piece_selected = None
                                    break
                if not have_move and piece != None and piece.color == turn:
                    piece_selected = piece
                    screen_update(board,piece_selected.movement_list)
                have_move = False
            else:
                board = [ # set the grid to the correct start position
                        [Rook("B",[0,0],"piece\\tour_noir.png",0),Knight("B",[0,1],"piece\\cavalier_noir.png",0),Bishop("B",[0,2],"piece\\fou_noir.png",0),Queen("B",[0,3],"piece\\dame_noir.png",0),King("B",[0,4],"piece\\roi_noir.png",0),Bishop("B",[0,5],"piece\\fou_noir.png",0),Knight("B",[0,6],"piece\\cavalier_noir.png",0),Rook("B",[0,7],"piece\\tour_noir.png",0)],
                        [Pawn("B",[1,0],"piece\\pion_noir.png",0),Pawn("B",[1,1],"piece\\pion_noir.png",0),Pawn("B",[1,2],"piece\\pion_noir.png",0),Pawn("B",[1,3],"piece\\pion_noir.png",0),Pawn("B",[1,4],"piece\\pion_noir.png",0),Pawn("B",[1,5],"piece\\pion_noir.png",0),Pawn("B",[1,6],"piece\\pion_noir.png",0),Pawn("B",[1,7],"piece\\pion_noir.png",0)],
                        [None,None,None,None,None,None,None,None], 
                        [None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None],
                        [Pawn("W",[6,0],"piece\\pion_blanc.png",0),Pawn("W",[6,1],"piece\\pion_blanc.png",0),Pawn("W",[6,2],"piece\\pion_blanc.png",0),Pawn("W",[6,3],"piece\\pion_blanc.png",0),Pawn("W",[6,4],"piece\\pion_blanc.png",0),Pawn("W",[6,5],"piece\\pion_blanc.png",0),Pawn("W",[6,6],"piece\\pion_blanc.png",0),Pawn("W",[6,7],"piece\\pion_blanc.png",0)],
                        [Rook("W",[7,0],"piece\\tour_blanc.png",0),Knight("W",[7,1],"piece\\cavalier_blanc.png",0),Bishop("W",[7,2],"piece\\fou_blanc.png",0),Queen("W",[7,3],"piece\\dame_blanc.png",0),King("W",[7,4],"piece\\roi_blanc.png",0),Bishop("W",[7,5],"piece\\fou_blanc.png",0),Knight("W",[7,6],"piece\\cavalier_blanc.png",0),Rook("W",[7,7],"piece\\tour_blanc.png",0)]
                        ]
                second_board = [ # set the grid to the correct start position
                        [Rook("B",[0,0],"piece\\tour_noir.png",0),Knight("B",[0,1],"piece\\cavalier_noir.png",0),Bishop("B",[0,2],"piece\\fou_noir.png",0),Queen("B",[0,3],"piece\\dame_noir.png",0),King("B",[0,4],"piece\\roi_noir.png",0),Bishop("B",[0,5],"piece\\fou_noir.png",0),Knight("B",[0,6],"piece\\cavalier_noir.png",0),Rook("B",[0,7],"piece\\tour_noir.png",0)],
                        [Pawn("B",[1,0],"piece\\pion_noir.png",0),Pawn("B",[1,1],"piece\\pion_noir.png",0),Pawn("B",[1,2],"piece\\pion_noir.png",0),Pawn("B",[1,3],"piece\\pion_noir.png",0),Pawn("B",[1,4],"piece\\pion_noir.png",0),Pawn("B",[1,5],"piece\\pion_noir.png",0),Pawn("B",[1,6],"piece\\pion_noir.png",0),Pawn("B",[1,7],"piece\\pion_noir.png",0)],
                        [None,None,None,None,None,None,None,None], 
                        [None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None],
                        [Pawn("W",[6,0],"piece\\pion_blanc.png",0),Pawn("W",[6,1],"piece\\pion_blanc.png",0),Pawn("W",[6,2],"piece\\pion_blanc.png",0),Pawn("W",[6,3],"piece\\pion_blanc.png",0),Pawn("W",[6,4],"piece\\pion_blanc.png",0),Pawn("W",[6,5],"piece\\pion_blanc.png",0),Pawn("W",[6,6],"piece\\pion_blanc.png",0),Pawn("W",[6,7],"piece\\pion_blanc.png",0)],
                        [Rook("W",[7,0],"piece\\tour_blanc.png",0),Knight("W",[7,1],"piece\\cavalier_blanc.png",0),Bishop("W",[7,2],"piece\\fou_blanc.png",0),Queen("W",[7,3],"piece\\dame_blanc.png",0),King("W",[7,4],"piece\\roi_blanc.png",0),Bishop("W",[7,5],"piece\\fou_blanc.png",0),Knight("W",[7,6],"piece\\cavalier_blanc.png",0),Rook("W",[7,7],"piece\\tour_blanc.png",0)]
                        ]

                turn = "W"
                print_board()
                update_movement(board,turn,[])
                print_piece(board)
                pygame.display.flip() # We actualize the screen with all the modification
                list_of_move = []
                piece_selected = None
                have_move = False
                game_end = False