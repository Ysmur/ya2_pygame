import pygame
# инициализация Pygame:
pygame.init()
# размеры окна:
n = int(input())
k = int(input())
size = width, height = n * k * 2, n * k * 2
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
# формирование кадра:
# команды рисования на холсте


def draw():
    red = pygame.Color('red')
    blue = pygame.Color('blue')
    green = pygame.Color('green')
    color_list = [blue, green, red]
    for i in range(k):
        pygame.draw.ellipse(screen, color_list[i % 3],
                            (0 + i*n, 0 + i*n, width - 2 * i * n, height - 2 * i * n), 0)


draw()
# смена (отрисовка) кадра:
pygame.display.flip()
# ожидание закрытия окна:
while pygame.event.wait().type != pygame.QUIT:
    pass
# завершение работы:
pygame.quit()