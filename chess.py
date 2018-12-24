import pygame
# инициализация Pygame:
pygame.init()
w, n = [int(x) for x in input().split()]
# размеры окна:
size = w, w
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
# формирование кадра:
# команды рисования на холсте


def draw():
    cell = 0
    if n % 2 != 0:
        for i in range(0, w, w//n):
            for j in range(0, w, w//n):
                if cell == 0:
                    pygame.draw.rect(screen, pygame.Color('black'), (i, j, w//n, w//n), 0)
                    cell = 1
                else:
                    pygame.draw.rect(screen, pygame.Color('white'), (i, j, w // n, w // n), 0)
                    cell = 0
    elif n % 2 == 0:
        cell = 1
        for i in range(0, w, w//n):
            for j in range(0, w, w//n):
                if cell == 0:
                    pygame.draw.rect(screen, pygame.Color('black'), (i, j, w//n, w//n), 0)
                    cell = 1
                else:
                    pygame.draw.rect(screen, pygame.Color('white'), (i, j, w // n, w // n), 0)
                    cell = 0
            cell += 1
            cell %= 2







draw()
# смена (отрисовка) кадра:
pygame.display.flip()
# ожидание закрытия окна:
while pygame.event.wait().type != pygame.QUIT:
    pass
# завершение работы:
pygame.quit()