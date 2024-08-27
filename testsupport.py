import random
import pygame
import sys
from pygame.locals import *

#초기화
pygame.init()

#화면
screen_width = 1280
screen_height = 640
screensize = [window_width, window_height]
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Crazy Arcade by RoDeLa")

character = pygame.image.load("./image/Bezzi.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0

is_game_running = True

while is_game_running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            is_game_running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                to_x -= 2 
            if event.key == pygame.K_RIGHT:
                to_x += 2  
            if event.key == pygame.K_UP:
                to_y -= 2 
            if event.key == pygame.K_DOWN: 
                to_y += 2  

character_x_pos += to_x
character_y_pos += to_y

if character_x_pos < 0:
    character_x_pos = 0
elif character_x_pos > screen_width - character_height:
    character_y_pos = screen_height

screen.blit(image_file, (0, 0))
screen.blit(character, (character_x_pos, character_y_pos))
pygame.display.update()

pygame.quit()



