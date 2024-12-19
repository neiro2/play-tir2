import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Игра Тир')

icon = pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)

target_image = pygame.image.load('img/target.png')
target_width = 80
target_height = 80

# Создаем список мишеней
targets = []
num_targets = 5

for _ in range(num_targets):
    target = {
        'x': random.randint(0, SCREEN_WIDTH - target_width),
        'y': random.randint(0, SCREEN_HEIGHT - target_height),
        'color': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        'points': random.randint(1, 10)
    }
    targets.append(target)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

misses = 0
score = 0

running = True
while running:
    screen.fill(color)  # очищаем экран

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            hit = False
            for target in targets:
                if target['x'] < mouse_x < target['x'] + target_width and target['y'] < mouse_y < target[
                    'y'] + target_height:
                    score += target['points']
                    # Перемещаем мишень в новое случайное место
                    target['x'] = random.randint(0, SCREEN_WIDTH - target_width)
                    target['y'] = random.randint(0, SCREEN_HEIGHT - target_height)
                    hit = True
                    break
            if not hit:
                misses += 1
                if misses >= 3:
                    print("Игра окончена!")
                    running = False

    # Отрисовываем мишени
    for target in targets:
        pygame.draw.rect(screen, target['color'], (target['x'], target['y'], target_width, target_height))

    pygame.display.update()

pygame.quit()