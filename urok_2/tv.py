import pygame
import random
# инициализация Pygame:
pygame.init()
# размеры окна:
size = width, height = 800, 600
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
# формирование кадра:
# команды рисования на холсте


def draw():
    screen.fill((0, 0, 0))
    h = random.random() * height
    h1 = random.random() * height
    h2 = random.random() * height
    pygame.draw.line(screen, (255, 255, 255), (0, h), (width, h), 5)
    pygame.draw.line(screen, (255, 255, 255), (0, h1), (width, h1), 4)
    pygame.draw.line(screen, (255, 255, 255), (0, h2), (width, h2), 3)


running = True
x = 1
while running:
    # внутри игрового цикла ещё один цикл
    # приема и обработки сообщений
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False

    # отрисовка и изменение свойств объектов
    draw()

    # обновление экрана
    pygame.display.flip()
