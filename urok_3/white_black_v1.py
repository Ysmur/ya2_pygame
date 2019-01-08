import pygame


pygame.init()
size = 501, 501
screen = pygame.display.set_mode(size)


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 50
        self.top = 10
        self.cell_size = 30

    def render(self):
        colors = [pygame.Color('black'), pygame.Color('white')]
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, colors[self.board[j][i]], (self.left + i * self.cell_size,
                                                                    self.top + j * self.cell_size,
                                                                    self.cell_size, self.cell_size))
                pygame.draw.rect(screen, colors[1], (self.left + i * self.cell_size, self.top + j * self.cell_size,
                                                     self.cell_size, self.cell_size), 1)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    # возвращает координаты клетки по координатам мыши
    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    # изменяет клетку
    def on_click(self, cell_coords):
        if self.board[cell_coords[1]][cell_coords[0]] == 1:
            self.board[cell_coords[1]][cell_coords[0]] = 0
        else:
            self.board[cell_coords[1]][cell_coords[0]] = 1

    # событие нажатие на кнопку мыши
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


# поле 5 на 7
board = Board(5, 7)
board.set_view(100, 100, 50)
running = True

while running:
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
pygame.quit()
