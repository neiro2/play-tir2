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
        'speed_x': random.choice([-0.5 -0.2, -0,1, 0,1, 0.2, 0.5]),  # случайная скорость по оси X
        'speed_y': random.choice([-0.5 -0.2, -0,1, 0,1, 0.2, 0.5]),  # случайная скорость по оси Y
        'points': random.randint(1, 10)
    }
    targets.append(target)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# Инициализация шрифта
font = pygame.font.Font(None, 36)

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
        'speed_x': random.choice([-0.5 - 0.2, -0, 1, 0, 1, 0.2, 0.5]),  # случайная скорость по оси X
        'speed_y': random.choice([-0.5 - 0.2, -0, 1, 0, 1, 0.2, 0.5]),  # случайная скорость по оси Y
        'points': random.randint(1, 10)
    }
    targets.append(target)

    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

misses = 0
score = 0


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

    # Обновляем позиции мишеней
    for target in targets:
        target['x'] += target['speed_x']
        target['y'] += target['speed_y']

        # Проверяем столкновение с границами экрана и изменяем направление
        if target['x'] <= 0 or target['x'] + target_width >= SCREEN_WIDTH:
            target['speed_x'] = -target['speed_x']
        if target['y'] <= 0 or target['y'] + target_height >= SCREEN_HEIGHT:
            target['speed_y'] = -target['speed_y']

        # Отрисовываем мишени
        screen.blit(target_image, (target['x'], target['y']))

    # Отображаем счет и количество промахов
    score_text = font.render(f'Счет: {score}', True, (255, 255, 255))
    misses_text = font.render(f'Промахи: {misses}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(misses_text, (10, 50))

    pygame.display.update()

pygame.quit()