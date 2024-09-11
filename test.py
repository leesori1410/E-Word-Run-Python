import pygame

# 초기화
pygame.init()

# 색상 설정
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 화면 크기 설정
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 플레이어 설정
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# 게임 루프를 제어하는 변수
running = True

# 게임 루프
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # 화면 밖으로 나가는 것 방지
    if player_x < 0:
        player_x = 0
    if player_x > screen_width - player_width:
        player_x = screen_width - player_width
    if player_y < 0:
        player_y = 0
    if player_y > screen_height - player_height:
        player_y = screen_height - player_height

    # 화면을 흰색으로 지우기
    screen.fill(WHITE)

    # 플레이어 그리기
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))

    # 화면 업데이트
    pygame.display.flip()

    # 프레임 조절
    pygame.time.Clock().tick(60)

# 게임 종료
pygame.quit()
