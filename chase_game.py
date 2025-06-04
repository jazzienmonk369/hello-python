# Verzija 1.1 - Dodat komentar u koduimport pygame
import random

# Inicijalizacija
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Juri me ako možeš!")
clock = pygame.time.Clock()

# Igrač i AI kvadrati
player = pygame.Rect(50, 50, 40, 40)
enemy = pygame.Rect(400, 400, 40, 40)
speed = 5
ai_speed = 2

run = True
while run:
    clock.tick(30)  # 30 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Kontrole
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= speed
    if keys[pygame.K_RIGHT]: player.x += speed
    if keys[pygame.K_UP]: player.y -= speed
    if keys[pygame.K_DOWN]: player.y += speed

    # AI logika - prati igrača
    if enemy.x < player.x: enemy.x += ai_speed
    if enemy.x > player.x: enemy.x -= ai_speed
    if enemy.y < player.y: enemy.y += ai_speed
    if enemy.y > player.y: enemy.y -= ai_speed

    # Prikaz
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (0, 255, 0), player)
    pygame.draw.rect(screen, (255, 0, 0), enemy)
    pygame.display.flip()

pygame.quit()