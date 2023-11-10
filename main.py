import pygame
from piece import *
from grid import *

pygame.init() #initalize pygame 
screen = pygame.display.set_mode((600,600)) # set the size of the window
pygame.display.set_caption("echec") # set the name 

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
