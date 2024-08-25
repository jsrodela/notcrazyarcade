import pygame

## Pygame 초기화
pygame.init()

## 화면 크기 설정 (가로 640, 세로 480)
screen = pygame.display.set_mode((640, 480))

## 창 제목 설정
pygame.display.set_caption("Pygame Test")

## 색상 정의 (RGB 값)
WHITE = (255, 255, 255)

## 메인 루프
running = True
while running:
    ## 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    ## 화면을 하얀색으로 채움
    screen.fill(WHITE)
    
    ## 화면 업데이트
    pygame.display.flip()

## Pygame 종료
pygame.quit()