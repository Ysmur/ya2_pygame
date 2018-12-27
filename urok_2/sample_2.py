import pygame
import random
# инициализация Pygame:
pygame.init()
# размеры окна:
size = width, height = 800, 600
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
# метод clock.tick() возвращает количество миллисекунд, прошедших с момента последнего вызова
clock = pygame.time.Clock()
# формирование кадра:
# команды рисования на холсте


def draw():
    pass


running = True
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
