import pygame


pygame.init()
size = 301, 301
screen = pygame.display.set_mode(size)


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def render(self):
        pygame.draw.rect(screen, pygame.Color('red'), (self.left, self.top, self.cell_size, self.cell_size), 0)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size


# поле 5 на 7
board = Board(5, 7)
board.set_view(100, 100, 50)
running = True

while running:
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
pygame.quit()
