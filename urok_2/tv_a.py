import pygame
import random


def draw():
    for i in range(10000):
        screen.fill(pygame.Color('white'), (random.random() * width, random.random() * height, 1, 1))


size = width, height = 301, 301
screen = pygame.display.set_mode(size)

running = True
while running:
    # внутри игрового цикл еще один цикл
    # приема и обработки сообщений
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False

    # отрисовка и изменение свойств объектов
    screen.fill((0, 0, 0))
    draw()

    # обновление экрана
    pygame.display.flip()

pygame.quit()