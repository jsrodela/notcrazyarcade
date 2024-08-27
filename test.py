import random
import pygame
from pygame.locals import *

#게임 초기화
pygame.init()

#디스플레이
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Crazy Arcade by RoDeLa V7")

#변수설정
clock = pygame.time.Clock()
FPS = 30

title_font = pygame.font.Font(None,120)
menu_font = pygame.font.Font(None,70)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

#배경
background = pygame.image.load("./image/Map.jpg")

#캐릭터 이미지
character = pygame.image.load("./image/Bezzi.png")
character_size = character.get_rect().size 
character_width = character_size[0] 
character_height = character_size[0.5
]

#캐릭터의 기준 좌표
character_x_pos = (screen_width / 2) - (character_width / 2)  #화면 중앙 (가로,세로/2)에 위치
character_y_pos = (screen_height / 2) - (character_height / 2)  

# 캐릭터 이동 좌표
to_x = 0
to_y = 0

# 캐릭터 이동 속도 변수
character_speed = 1


#적
class Enemy:
    def __init__(self):
        self.image = pygame.image.load("./image/Badguy.png")
        self.size = self.image.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.x = random.randint(0, screen_width - self.width)
        self.y = 0  #화면 위에서 생성
        self.speed = random.randint(1, 3)  #속도 1-3
        self.direction_x = random.choice([-1, 1])  
        self.direction_y = 1 
    
    #적 위치 업데이트
    def update(self):
        self.x += self.direction_x * self.speed
        self.y += self.direction_y * self.speed
        
        #화면경계 넘지않게
        if self.x <= 0 or self.x >= screen_width - self.width:
            self.direction_x *= -1
        
        #화면에 나타냄
        screen.blit(self.image, (self.x, self.y))
    
    def collide(self, player_rect):
        enemy_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return enemy_rect.colliderect(player_rect)

#적 리스트
enemies = []
enemy_spawn_timer = 0 
    
# 이벤트 루프
running = True 
while running:
    dt = clock.tick(30) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_LEFT:  
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: 
                to_x += character_speed
            elif event.key == pygame.K_DOWN:  
                to_y += character_speed
            elif event.key == pygame.K_UP: 
                to_y -= character_speed

        if event.type == pygame.KEYUP:  #방향키를 뗐을 때 캐릭터 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
                

    #캐릭터 위치 업데이트
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #왼쪽, 오른쪽 경계
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #위, 아래 경계
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
        
    #적 스폰타이머(3초)
    enemy_spawn_timer =+dt
    if enemy_spawn_timer >= 3000:
        enemies.append(Enemy())
        enemy_spawn_timer = 0
        
    #캐릭터 그리기,배경 그리기
    character_rect = pygame.Rect(character_x_pos, character_y_pos, character_width, character_height)
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(background, (0, 0))
    
    #충돌 감지
    for enemy in enemies:
        enemy.update()
        if enemy.collide(character_rect):
            running = False

    #화면 업데이트
    pygame.display.update()

#게임 종료
pygame.quit()
sys.exit()

    