import pygame
from sys import exit
import copy


def print_board () :
    axis_value = [0,75,150,225,300,375,450,525]
    color_value = 0 
    for y in axis_value :
        for x in axis_value :
            if color_value == 0 :
                pygame.draw.rect(screen,"white",[x,y,75,75])
                if x != 525 :
                    color_value = 1
            elif color_value== 1 :
                pygame.draw.rect(screen,"black",[x,y,75,75])
                if x != 525:
                    color_value = 0

def print_piece (grid:list) :
    axis_value = [0,75,150,225,300,375,450,525]
    for row_number,row in enumerate(grid):
        for column,piece in enumerate(row) :
            if piece[0] == "W":
                if piece[1] == "T" :
                    white_tower_surf = white_tower_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5))
                    screen.blit(white_tower_sprite,white_tower_surf)
                if piece[1] == "N" :
                    white_knight_surf = white_knight_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5))
                    screen.blit(white_knight_sprite,white_knight_surf)
                if piece[1] == "B" :
                    white_bishop_surf = white_bishop_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5))
                    screen.blit(white_bishop_sprite,white_bishop_surf)
                if piece[1] == "Q" :
                    white_queen_surf = white_queen_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5))
                    screen.blit(white_queen_sprite,white_queen_surf)
                if piece[1] == "K" :
                    white_king_surf = white_king_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5))
                    screen.blit(white_king_sprite,white_king_surf)
                if piece[1] == "P" :
                    white_pawn_surf = white_pawn_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5))
                    screen.blit(white_pawn_sprite,white_pawn_surf)
            elif piece[0] =="B" :
                if piece[1] == "T" :
                    black_tower_surf = black_tower_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5))
                    screen.blit(black_tower_sprite,black_tower_surf)
                if piece[1] == "N" :    
                    black_knight_surf = black_knight_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5))
                    screen.blit(black_knight_sprite,black_knight_surf)
                if piece[1] == "B" :
                    black_bishop_surf = black_bishop_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5))
                    screen.blit(black_bishop_sprite,black_bishop_surf)
                if piece[1] == "Q" :
                    black_queen_surf = black_queen_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5))
                    screen.blit(black_queen_sprite,black_queen_surf)
                if piece[1] == "K" :
                    black_king_surf = black_king_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5))
                    screen.blit(black_king_sprite,black_king_surf)
                if piece[1] == "P" :
                    black_pawn_surf = black_pawn_sprite.get_rect(center = (axis_value[column]+37.5,axis_value[row_number]+37.5))
                    screen.blit(black_pawn_sprite,black_pawn_surf)

def where_am_i (mouse_pos:list):
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
    pos = [y,x]
    return pos

def show_possibilty(grid:list,position:list,turn):
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
    plays,selected_piece = mouvement(grid,position,turn)
    for play in plays :
        mouvement_grid[play[0]][play[1]] = "Y"
    return selected_piece,mouvement_grid

def mouvement(grid:list,position:list,turn:int) :
    piece = grid[position[0]][position[1]]
    type_of_piece = piece[1]
    color_of_piece = piece[0]
    plays_allowed = []
    plays_tempory_allowed = []
    stock_of_play = []
    final_play = []
    if type_of_piece == "T":
        mur = True
        for x_value,piece in enumerate(grid[position[0]]):
            if mur == True :
                    if piece == "--":
                        plays_tempory_allowed.append([position[0],x_value])
                    else:
                        if x_value < position[1]:
                            plays_tempory_allowed.clear()
                            plays_tempory_allowed.append([position[0],x_value])
                        if x_value > position[1]:
                            plays_tempory_allowed.append([position[0],x_value])
                            mur = False 
            
        for plays in plays_tempory_allowed:
            plays_allowed.append(plays)
        plays_tempory_allowed.clear()
        stock_of_play.clear()
        mur = True
        for line in range(len(grid)):
            stock_of_play.append(grid[line][position[1]])
        for y_value,piece in enumerate(stock_of_play):
            if mur == True :
                if piece == "--":
                    plays_tempory_allowed.append([y_value,position[1]])
                else:
                    if y_value < position[0]:
                        plays_tempory_allowed.clear()
                        plays_tempory_allowed.append([y_value,position[1]])
                    if y_value > position[0]:
                        plays_tempory_allowed.append([y_value,position[1]])
                        mur = False
        for plays in plays_tempory_allowed:
            plays_allowed.append(plays)
            
    if type_of_piece == "B":
            mur = True
            stock_of_play = diagonale_right(position)
            for play in stock_of_play:
                if mur == True :
                    if grid[play[0]][play[1]] == "--":
                        plays_tempory_allowed.append(play)
                    else:
                        if play[1] < position[1]:
                            plays_tempory_allowed.clear()
                            plays_tempory_allowed.append(play)
                        if play[1] > position[1]:
                            plays_tempory_allowed.append(play)
                            mur = False
                    
            for plays in plays_tempory_allowed:
                plays_allowed.append(plays)
            plays_tempory_allowed.clear()
            
            stock_of_play = diagonale_left(position)
            mur = True
            for play in stock_of_play:
                if mur == True :
                    if grid[play[0]][play[1]] == "--":
                        plays_tempory_allowed.append(play)
                    else:
                        if play[1] < position[1]:
                            plays_tempory_allowed.clear()
                            plays_tempory_allowed.append(play)
                        if play[1] > position[1]:
                            plays_tempory_allowed.append(play)
                            mur = False
            for plays in plays_tempory_allowed:
                plays_allowed.append(plays)
            plays_tempory_allowed.clear()
    stock_of_play.clear()
    if type_of_piece == "Q":
        mur = True
        stock_of_play = diagonale_right(position)
        for play in stock_of_play:
            if mur == True :
                if grid[play[0]][play[1]] == "--":
                    plays_tempory_allowed.append(play)
                else:
                    if play[1] < position[1]:
                        plays_tempory_allowed.clear()
                        plays_tempory_allowed.append(play)
                    if play[1] > position[1]:
                        plays_tempory_allowed.append(play)
                        mur = False
        
        for plays in plays_tempory_allowed:
            plays_allowed.append(plays)
        plays_tempory_allowed.clear()
        mur = True

        stock_of_play = diagonale_left(position)
        for play in stock_of_play:
            if mur == True :
                if grid[play[0]][play[1]] == "--":
                    plays_tempory_allowed.append(play)
                else:
                    if play[1] < position[1]:
                        plays_tempory_allowed.clear()
                        plays_tempory_allowed.append(play)
                    if play[1] > position[1]:
                        plays_tempory_allowed.append(play)
                        mur = False
        for plays in plays_tempory_allowed:
            plays_allowed.append(plays)
        plays_tempory_allowed.clear()
        stock_of_play.clear()
        
        mur = True
        for x_value,piece in enumerate(grid[position[0]]):
            if mur == True :
                    if piece == "--":
                        plays_tempory_allowed.append([position[0],x_value])
                    else:
                        if x_value < position[1]:
                            plays_tempory_allowed.clear()
                            plays_tempory_allowed.append([position[0],x_value])
                        if x_value > position[1]:
                            plays_tempory_allowed.append([position[0],x_value])
                            mur = False 
            
        for plays in plays_tempory_allowed:
            plays_allowed.append(plays)
        plays_tempory_allowed.clear()

        mur = True
        for line in range(len(grid)):
            stock_of_play.append(grid[line][position[1]])
        for y_value,piece in enumerate(stock_of_play):
            if mur == True :
                if piece == "--":
                    plays_tempory_allowed.append([y_value,position[1]])
                else:
                    if y_value < position[0]:
                        plays_tempory_allowed.clear()
                        plays_tempory_allowed.append([y_value,position[1]])
                    if y_value > position[0]:
                        plays_tempory_allowed.append([y_value,position[1]])
                        mur = False
        for plays in plays_tempory_allowed:
            plays_allowed.append(plays)
    if type_of_piece == "K":
            plays_allowed.append([position[0]+1,position[1]+1])
            plays_allowed.append([position[0],position[1]+1])
            plays_allowed.append([position[0]+1,position[1]])
            plays_allowed.append([position[0],position[1]-1])
            plays_allowed.append([position[0]-1,position[1]])
            plays_allowed.append([position[0]-1,position[1]+1])
            plays_allowed.append([position[0]+1,position[1]-1])
            plays_allowed.append([position[0]-1,position[1]-1])
    if type_of_piece == "N":
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
            if play[0] >= 0 and play[0] < 8 and play[1] >= 0 and play[1] < 8: 
                if color_of_piece=="W":
                    if grid[play[0]][play[1]][0] != "W" :
                        final_play.append(play)
    else :
        for play in plays_allowed :
            if play[0] >= 0 and play[0] < 8 and play[1] >= 0 and play[1] < 8: 
                if color_of_piece=="B":
                    if grid[play[0]][play[1]][0] != "B" :
                        final_play.append(play)   
    return final_play,position

def can_moove (position:list,old_mouvement_grid):
    if mouvement_grid[position[0]][position[1]] == "Y":
        return True
    return False

def play(position, grid_of_the_game, selected_piece):
    which_piece = None
    piece = grid_of_the_game[selected_piece[0]][selected_piece[1]]
    grid_of_the_game[position[0]][position[1]] = piece
    grid_of_the_game[selected_piece[0]][selected_piece[1]] = "--"
    if grid_of_the_game[position[0]][position[1]][1] == "P":
        if grid_of_the_game[position[0]][position[1]][0] == "W":
            if position[0] == 0:
                while which_piece !="Q" and which_piece !="T" and which_piece !="B" and which_piece != "N" : 
                    which_piece = str(input("en qu'elle piece veut tu transformer ton pion ? : \nEntre Q pour une dame\nEntre T pour une tour\nEntre N pour un cavalier\nEntre B pour un fou\n alors tu choisis quoi ? : "))
                piece = "W"+which_piece
                grid_of_the_game[position[0]][position[1]] = str(piece)
        else:
            if position[0] == 7:
                while which_piece !="Q" and which_piece !="T" and which_piece !="B" and which_piece != "N" : 
                    which_piece = str(input("en qu'elle piece veut tu transformer ton pion ? : \nEntre Q pour une dame\nEntre T pour une tour\nEntre N pour un cavalier\nEntre B pour un fou\n alors tu choisis quoi ? : "))
                piece = "B"+which_piece
                grid_of_the_game[position[0]][position[1]] = str(piece)
    
    return grid_of_the_game

def change_turn(turn:int):
    if turn == 1 :
        return 0
    else :
        return 1

def display_possibilty (mouvement_grid:list) :
    axis_value = [0,75,150,225,300,375,450,525]
    color_value = 0 
    for y,line in enumerate(mouvement_grid) :
        for x,column in enumerate(line) :
            if  column == "Y":
                pygame.draw.rect(screen,"yellow",[axis_value[x],axis_value[y],75,75])
            if column =="R" :
                pygame.draw.rect(screen,"Red",[axis_value[x],axis_value[y],75,75])

def diagonale_right (position:list):
    plays = []
    y = position[0]
    x = position[1]
    while x > 0 and y > 0 :
        x -= 1
        y -= 1
        plays.append([y,x])
    plays = list(reversed(plays))
    y = position[0]
    x = position[1]
    while x < 7 and y < 7 :
        x += 1
        y += 1
        plays.append([y,x])
    return plays

def diagonale_left (position:list) :
    plays = []
    y = position[0]
    x = position[1]
    while x >= 0 and y < 7 :
        x -= 1
        y += 1
        plays.append([y,x])
    plays = list(reversed(plays))
    y = position[0]
    x = position[1]
    while x < 7 and y > 0 :
        y -= 1
        x += 1
        plays.append([y,x])
    return plays

def there_is_a_check(position,grid,selected_piece,turn):
    
    fake_grid = copy.deepcopy(grid)
    piece = grid[selected_piece[0]][selected_piece[1]]
    fake_grid[position[0]][position[1]] = piece
    fake_grid[selected_piece[0]][selected_piece[1]] = "--"
    check_list = []
    random_piece = None
    check = None
    check,random_piece = check_for_a_check(fake_grid,turn)
    return check,random_piece

def check_for_a_check(fake_grid,turn):
    random_piece = None
    for line in range(len(fake_grid)):
            for piece in range(len(fake_grid[line])):
                if turn == 0 :
                    if fake_grid[line][piece][0] == "B":
                        list_of_plays,random_piece = mouvement(fake_grid,[line,piece],1)
                        for plays in list_of_plays:
                            if fake_grid[plays[0]][plays[1]] == "WK":
                                return True,random_piece
                else :
                    if fake_grid[line][piece][0] == "W":
                        list_of_plays,random_piece = mouvement(fake_grid,[line,piece],0)
                        for plays in list_of_plays:
                            if fake_grid[plays[0]][plays[1]] == "BK":
                                return True,random_piece
    return False,random_piece

def check_mate(turn,grid):
    where_king_can_go  = None
    position_to_go = []
    where_does_my_piece_can_go = []
    if turn == 1:
        check,random_piece = check_for_a_check(grid,0)
        for line in range(len(grid)):
            for piece in range(len(grid[line])):
                if grid[line][piece] == "WK":
                    position = [line,piece]
                else:
                    if grid[line][piece][0] == "W":
                        position_of_white_piece = [line,piece]
                        where_my_piece_can_go,random_piece = mouvement(grid,position_of_white_piece,0)
                        for mouvement_of_piece in where_my_piece_can_go:
                            where_does_my_piece_can_go.append(mouvement_of_piece)
        where_king_can_go,selected_piece = mouvement(grid,position,0)
        for plays in where_king_can_go:
            check,random_piece = there_is_a_check(plays,grid,selected_piece,0)
            if check == False:
                return False
        check,position_of_the_piece_who_moove = check_for_a_check(grid,0)
        piece = grid[position_of_the_piece_who_moove[0]][position_of_the_piece_who_moove[1]]
        if where_does_my_piece_can_go != []:
            if piece[1] == "T" or piece[1] == "Q":
                if position_of_the_piece_who_moove[0] == position[0] :
                    if position_of_the_piece_who_moove[1] < position[1] :
                        difference = position[1]-position_of_the_piece_who_moove[1]-1
                        for value in range(1,difference):
                            position_to_go.append([position[0],position[1]+value])
                    else:
                        difference = position_of_the_piece_who_moove[1]-1-position[1]
                        for value in range(1,difference):
                            position_to_go.append([position[0],position[1]+value])
                elif position_of_the_piece_who_moove[1] == position[1]:
                    if position_of_the_piece_who_moove[0] < position[0] :
                        difference = position[0]-position_of_the_piece_who_moove[0]-1
                        for value in range(1,difference):
                            position_to_go.append([position[0]+value,position[1]])
                    else:
                        difference = position_of_the_piece_who_moove[0]-1-position[0]
                        for value in range(1,difference):
                            position_to_go.append([position[0]+value,position[1]])
            if piece[1] == "B" or piece[1] == "Q":
                if position[0]<position_of_the_piece_who_moove[0] :
                    if position[1]<position_of_the_piece_who_moove[1]:
                        difference = position_of_the_piece_who_moove[0]-position[0]
                        for value in range(1,difference):
                            position_to_go.append([value+position[0],value+position[1]])
                    else :
                        difference = position_of_the_piece_who_moove[0]-position[0]-1
                        for value in range(difference):
                            position_to_go.append([value+position[0],-value+position[1]])
                else :
                    if position[1]<position_of_the_piece_who_moove[1]:
                        difference = position[0]-position_of_the_piece_who_moove[0]
                        for value in range(1,difference):
                            position_to_go.append([value+position[0],value+position[1]])
                    else :
                        difference = position[0]-1-position_of_the_piece_who_moove[0]
                        for value in range(difference):
                            position_to_go.append([value+position[0],-value+position[1]])
            position_to_go.append([position_of_the_piece_who_moove[0],position_of_the_piece_who_moove[1]])
            for play in where_does_my_piece_can_go:
                for go_here in position_to_go:
                    if play[0]==go_here[0]:
                        if play[1] == go_here[1]:
                            return False
        else :
            if check == False :
                return("pat")
    else :
        check,random_piece = check_for_a_check(grid,1)
        for line in range(len(grid)):
            for piece in range(len(grid[line])):
                if grid[line][piece] == "BK":
                    position = [line,piece]
                else:
                    if grid[line][piece][0] == "B":
                        position_of_black_piece = [line,piece]
                        where_my_piece_can_go,random_piece = mouvement(grid,position_of_black_piece,1)
                        for mouvement_of_piece in where_my_piece_can_go:
                            where_does_my_piece_can_go.append(mouvement_of_piece)
        where_king_can_go,selected_piece = mouvement(grid,position,1)
        for plays in where_king_can_go:
            check,randown_piece = there_is_a_check(plays,grid,selected_piece,1)
            if check == False:
                return False
        check,position_of_the_piece_who_moove = check_for_a_check(grid,1)
        piece = grid[position_of_the_piece_who_moove[0]][position_of_the_piece_who_moove[1]]
        if where_does_my_piece_can_go != []:
            if piece[1] == "T" or piece[1] == "Q":
                if position_of_the_piece_who_moove[0] == position[0] :
                    if position_of_the_piece_who_moove[1] < position[1] :
                        difference = position[1]-position_of_the_piece_who_moove[1]-1
                        for value in range(1,difference):
                            position_to_go.append([position[0],position[1]+value])
                    else:
                        difference = position_of_the_piece_who_moove[1]-1-position[1]
                        for value in range(1,difference):
                            position_to_go.append([position[0],position[1]+value])
                elif position_of_the_piece_who_moove[1] == position[1]:
                    if position_of_the_piece_who_moove[0] < position[0] :
                        difference = position[0]-position_of_the_piece_who_moove[0]-1
                        for value in range(1,difference):
                            position_to_go.append([position[0]+value,position[1]])
                    else:
                        difference = position_of_the_piece_who_moove[0]-1-position[0]
                        for value in range(1,difference):
                            position_to_go.append([position[0]+value,position[1]])
            if piece[1] == "B" or piece[1] == "Q":
                if position[0]<position_of_the_piece_who_moove[0] :
                    if position[1]<position_of_the_piece_who_moove[1]:
                        difference = position_of_the_piece_who_moove[0]-position[0]
                        for value in range(1,difference):
                            position_to_go.append([value+position[0],value+position[1]])
                    else :
                        difference = position_of_the_piece_who_moove[0]-position[0]-1
                        for value in range(difference):
                            position_to_go.append([value+position[0],-value+position[1]])
                else :
                    if position[1]<position_of_the_piece_who_moove[1]:
                        difference = position[0]-position_of_the_piece_who_moove[0]
                        for value in range(1,difference):
                            position_to_go.append([value+position[0],value+position[1]])
                    else :
                        difference = position[0]-1-position_of_the_piece_who_moove[0]
                        for value in range(difference):
                            position_to_go.append([value+position[0],-value+position[1]])
            position_to_go.append([position_of_the_piece_who_moove[0],position_of_the_piece_who_moove[1]])
            for play in where_does_my_piece_can_go:
                for go_here in position_to_go:
                    if play[0]==go_here[0]:
                        if play[1] == go_here[1]:
                            return False
        else :
            if check == False :
                return("pat")
    if check == False :
        return False
    return True

def tie(grid) :
    white_piece = []
    black_piece = []
    for line in grid :
        for piece in line :
            if piece[0] == "W":
                white_piece.append(piece)
            elif piece[0] == "B":
                black_piece.append(piece)
    if enough_piece(white_piece) and enough_piece(black_piece) :
        return True 
    return False

def enough_piece(list:list) :
    compteur = 0
    for element in list :
        if element[1] == "Q" or element[1] == "T" or element[1] =="P" :
            return False
        if element[1] == "B" or element[1] == "N":
            compteur +=1
    if compteur > 1:
        return False
    return True

def print_the_rock(grid,turn,king_pos,king_next_pos,tower_pos,tower_next_pos):
    statement = False
    global game,selected_piece,mouvement_grid
    fake_grid = copy.deepcopy(grid)
    piece = fake_grid[king_pos[0]][king_pos[1]]
    fake_grid[king_next_pos[0]][king_next_pos[1]] = piece
    fake_grid[king_pos[0]][king_pos[1]] = "--"
    piece = fake_grid[tower_pos[0]][tower_pos[1]]
    fake_grid[tower_next_pos[0]][tower_next_pos[1]] = piece
    fake_grid[tower_pos[0]][tower_pos[1]] = "--"
    check,random_piece = check_for_a_check(fake_grid,turn)
    if check== False:
        statement = True
        grid = play(king_next_pos,grid,king_pos)
        grid = play(tower_next_pos,grid,tower_pos)
        mate = check_mate(turn,grid)
        if mate == True:
            game = False
        if mate == ("pat") :
            game = False
            print("Il y a pat :)")
        if tie(grid) :
            game = False
            print("Il y a egalité par manque de materiel :)")
        turn = change_turn(turn)
        selected_piece = None
        mouvement_grid = [["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"]]
    return statement,turn

def choose_where_rock(grid,turn,position) :
    statement = False
    if turn == 0:
        if position[1] == 0 :
            king_pos = [7,4]
            king_next_pos = [7,2]
            tower_pos = position
            tower_next_pos = [7,3]
            statement,turn = print_the_rock(grid,turn,king_pos,king_next_pos,tower_pos,tower_next_pos)
            return statement,turn
        if position[1] == 7 :
            king_pos = [7,4]
            king_next_pos = [7,6]
            tower_pos = position
            tower_next_pos = [7,5]
            statement,turn = print_the_rock(grid,turn,king_pos,king_next_pos,tower_pos,tower_next_pos)
            return statement,turn
    if turn == 1:
        if position[1] == 0 :
            king_pos = [0,4]
            king_next_pos = [0,2]
            tower_pos = position
            tower_next_pos = [0,3]
            statement,turn = print_the_rock(grid,turn,king_pos,king_next_pos,tower_pos,tower_next_pos)
            return statement,turn
        if position[1] == 7 :
            king_pos = [0,4]
            king_next_pos = [0,6]
            tower_pos = position
            tower_next_pos = [0,5]
            statement,turn = print_the_rock(grid,turn,king_pos,king_next_pos,tower_pos,tower_next_pos)
            return statement,turn
    return statement,turn
pygame.init() #initalize pygame 
screen = pygame.display.set_mode((600,600)) # set the size of the window
pygame.display.set_caption("echec") # set the name 
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
mouvement_grid = [
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
    if game :
        print_board()
        display_possibilty(mouvement_grid)
        print_piece(grid)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN : # if the player click
                    position = where_am_i(pygame.mouse.get_pos())
                    if can_moove(position,mouvement_grid) :
                        check,position_of_a_piece = there_is_a_check(position,grid,selected_piece,turn)
                        if check == False:
                            grid = play(position,grid,selected_piece)
                            
                            mate = check_mate(turn,grid)
                            if mate == True:
                                game = False
                            if mate == ("pat") :
                                game = False
                                print("Il y a pat :)")
                            if tie(grid) :
                                game = False
                                print("Il y a egalité par manque de materiel :)")
                            turn = change_turn(turn)
                            selected_piece = None
                            mouvement_grid = [["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"]]
                            if turn == 0 :
                                if grid[position[0]][position[1]] == "BK" :
                                    black_king_moove_counter += 1
                                elif grid[position[0]][position[1]] == "BT" :
                                    if position[1] == 0:
                                        black_left_tower_moove_counter += 1
                                    if position[1] == 6 :
                                        black_right_tower_moove_counter += 1
                            if turn == 1 :
                                if grid[position[0]][position[1]] == "WK" :
                                    white_king_moove_counter += 1
                                elif grid[position[0]][position[1]] == "WT" :
                                    if position[1] == 0:
                                        white_left_tower_moove_counter += 1
                                    if position[1] == 6 :
                                        white_right_tower_moove_counter += 1
                                        
                    elif mouvement_grid[position[0]][position[1]] == "R":
                        check,random_piece = check_for_a_check(grid,turn)
                        if check == False:
                            rock_statement,turn = choose_where_rock(grid,turn,position)
                            if rock_statement :
                                if turn == 0 :
                                    black_king_moove_counter += 1
                                if turn == 1 :
                                    white_king_moove_counter += 1
                    else :
                        selected_piece,mouvement_grid = show_possibilty(grid,position,turn)
                        if turn == 0 :
                            if grid[selected_piece[0]][selected_piece[1]] == "WK":
                                if white_king_moove_counter == 0 :
                                    if white_right_tower_moove_counter == 0 :
                                        if grid[7][1] == "--" and grid[7][2] == "--" and grid[7][3] == "--":
                                            mouvement_grid[7][0] = "R"
                                    if white_left_tower_moove_counter == 0 :
                                        if grid[7][5] == "--" and grid[7][6] == "--":
                                            mouvement_grid[7][7] = "R"
                        else :
                            if grid[selected_piece[0]][selected_piece[1]] == "BK":
                                if black_king_moove_counter == 0 :
                                    if black_right_tower_moove_counter == 0 :
                                        if grid[0][1] == "--" and grid[0][2] == "--" and grid[0][3] == "--":
                                            mouvement_grid[0][0] = "R"
                                    if black_left_tower_moove_counter == 0 :
                                        if grid[0][5] == "--" and grid[0][6] == "--":
                                            mouvement_grid[0][7] = "R"
                            
    else :
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
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
        print_board()
        print_piece(grid)
        
    pygame.display.flip()
    