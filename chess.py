import pygame
# инициализация Pygame:
pygame.init()
width, number = [int(x) for x in input().split()]
# размеры окна:
size = width, width
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
# формирование кадра:
# команды рисования на холсте


def draw():
    screen.fill((0, 0, 0))
    for i in range(width//number, width, width//number):
        




draw()
# смена (отрисовка) кадра:
pygame.display.flip()
# ожидание закрытия окна:
while pygame.event.wait().type != pygame.QUIT:
    pass
# завершение работы:
pygame.quit()