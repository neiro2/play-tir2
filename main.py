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


misses = 0
score = 0






running = True
while running:
    pass