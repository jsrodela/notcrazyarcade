import random
import pygame
import sys
from pygame.locals import *

# 초기화
pygame.init()

# 화면 설정
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Crazy Arcade by RoDeLa")

# FPS 설정
clock = pygame.time.Clock()
FPS = 30

# 배경 설정
try:
    background = pygame.image.load("./image/Map.jpg")
    background = pygame.transform.scale(background, (screen_width, screen_height))
except pygame.error as e:
    print(f"배경 이미지 로딩 실패: {e}")
    pygame.quit()
    sys.exit()

# 캐릭터 설정
try:
    character = pygame.image.load("./image/Bezzi.png")
except pygame.error as e:
    print(f"캐릭터 이미지 로딩 실패: {e}")
    pygame.quit()
    sys.exit()

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = (screen_height / 2)

# 이동 좌표 초기화
to_x = 0
to_y = 0

# 적 정의
class Enemy:
    def __init__(self):
        try:
            self.image = pygame.image.load("./image/Badguy.png")
            self.image_caught = pygame.image.load("./image/Captured.png")
        except pygame.error as e:
            print(f"적 이미지 로딩 실패: {e}")
            pygame.quit()
            sys.exit()

        self.size = self.image.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_height - self.height)
        self.speed = random.randint(1, 3)
        self.x_direction = random.choice([-1, 1])
        self.y_direction = random.choice([-1, 1])
        self.is_alive = True
        self.is_caught = False
        self.start_ticks = None
        self.time = 5

    def get_rect(self):
        # 히트박스를 줄이기 위해 조금 더 작은 사각형을 반환
        return pygame.Rect(self.x + 10, self.y + 10, self.width - 20, self.height - 20)

    def display(self):
        if self.is_caught:
            screen.blit(self.image_caught, (self.x, self.y))
        else:
            screen.blit(self.image, (self.x, self.y))

    def move(self):
        if not self.is_caught:
            self.x += self.speed * self.x_direction
            self.y += self.speed * self.y_direction

            # 경계 처리
            if self.x < 0 or self.x > screen_width - self.width:
                self.x_direction *= -1
            if self.y < 0 or self.y > screen_height - self.height:
                self.y_direction *= -1

    def update(self):
        if self.is_caught:
            elapsed_time = (pygame.time.get_ticks() - self.start_ticks) / 1000
            timer = self.time - elapsed_time
            if timer <= 0:
                self.is_caught = False
        self.display()
        self.move()

    def catch(self):
        self.is_caught = True
        self.start_ticks = pygame.time.get_ticks()

# 게임 루프
enemies = []  # 적 리스트 초기화

# 적 생성 타이머 설정
enemy_spawn_time = 0  # 다음 적 생성 시간
start_ticks = pygame.time.get_ticks()  # 게임 시작 시각

is_game_running = True
while is_game_running:
    current_ticks = pygame.time.get_ticks()
    elapsed_time = (current_ticks - start_ticks) / 1000  # 게임이 시작된 후 경과 시간

    # 적 생성 타이머 업데이트
    if elapsed_time >= enemy_spawn_time:
        enemies.append(Enemy())  # 새로운 적 생성
        enemy_spawn_time = elapsed_time + random.uniform(0, 2)  # 다음 적 생성 시간 업데이트

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                to_x = -8
            if event.key == pygame.K_RIGHT:
                to_x = 8  
            if event.key == pygame.K_UP:
                to_y = -8 
            if event.key == pygame.K_DOWN: 
                to_y = 8  

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 캐릭터 위치 업데이트
    character_x_pos += to_x
    character_y_pos += to_y

    # 경계 넘어가면 화면 중앙으로 이동
    if character_x_pos < 0:
        character_x_pos = (screen_width / 2) - (character_width / 2)
        character_y_pos = (screen_height / 2)
        
    elif character_x_pos > screen_width - character_width:
        character_x_pos = (screen_width / 2) - (character_width / 2)
        character_y_pos = (screen_height / 2)
        
    if character_y_pos < 0:
        character_y_pos = (screen_height / 2)
        character_x_pos = (screen_width / 2) - (character_width / 2)
        
    elif character_y_pos > screen_height - character_height:
        character_y_pos = (screen_height / 2)
        character_x_pos = (screen_width / 2) - (character_width / 2)

    # 화면 그리기
    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기

    # 적 업데이트 및 그리기
    for enemy in enemies:
        enemy.update()
        # 충돌 감지
        if enemy.get_rect().colliderect(pygame.Rect(character_x_pos, character_y_pos, character_width, character_height)):
            is_game_running = False

    pygame.display.update()  # 화면 업데이트
    clock.tick(FPS)  # FPS 조절

# 게임 종료 후 경과 시간 표시
screen.fill((0, 0, 0))  # 화면을 검정색으로 채우기
font = pygame.font.Font(None, 74)
text = font.render(f"Game Over! Time: {int(elapsed_time)}s", True, (255, 255, 255))
text_rect = text.get_rect(center=(screen_width / 2, screen_height / 2))
screen.blit(text, text_rect)
pygame.display.update()

# 종료 대기
pygame.time.wait(3000)  # 3초 동안 대기

pygame.quit()
sys.exit()
