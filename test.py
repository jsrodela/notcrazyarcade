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
        return pygame.Rect(self.x + 40, self.y + 40, self.width - 40, self.height - 40)

    def display(self):
        if self.is_caught:
            screen.blit(self.image_caught, (self.x, self.y))
        else:
            screen.blit(self.image, (self.x, self.y))

    def move(self):
        if not self.is_caught:
            self.x += self.speed * self.x_direction
            self.y += self.speed * self.y_direction

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

def reset_game():
    global character_x_pos, character_y_pos, to_x, to_y, enemies, start_ticks, is_game_running, enemy_spawn_time, final_time
    character_x_pos = (screen_width / 2) - (character_width / 2)
    character_y_pos = (screen_height / 2)
    to_x, to_y = 0, 0
    enemies = []
    start_ticks = pygame.time.get_ticks()
    enemy_spawn_time = 0
    is_game_running = True
    final_time = 0

reset_game()

while True:
    current_ticks = pygame.time.get_ticks()

    if is_game_running:
        elapsed_time = (current_ticks - start_ticks) / 1000

        if elapsed_time >= enemy_spawn_time:
            enemies.append(Enemy())
            enemy_spawn_time = elapsed_time + random.uniform(0, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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

        character_x_pos += to_x
        character_y_pos += to_y

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

        screen.blit(background, (0, 0))
        screen.blit(character, (character_x_pos, character_y_pos))

        for enemy in enemies:
            enemy.update()
            if enemy.get_rect().colliderect(pygame.Rect(character_x_pos, character_y_pos, character_width, character_height)):
                final_time = elapsed_time  # 게임 종료 시점의 시간을 저장
                is_game_running = False

        pygame.display.update()
        clock.tick(FPS)

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()

        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        text = font.render(f"Game Over! Time: {int(final_time)}s", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen_width / 2, screen_height / 2))
        screen.blit(text, text_rect)
        font_small = pygame.font.Font(None, 36)
        text_restart = font_small.render("Press 'R' to Restart", True, (255, 255, 255))
        text_restart_rect = text_restart.get_rect(center=(screen_width / 2, screen_height / 2 + 100))
        screen.blit(text_restart, text_restart_rect)
        pygame.display.update()
        clock.tick(FPS)