import pygame


pygame.init()
size = 420, 420
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Lines")
clock = pygame.time.Clock()


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
        colors = [pygame.Color(72, 91, 73), pygame.Color('white')]
        for i in range(self.width):
            for j in range(self.height):
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
        pass

    # событие нажатие на кнопку мыши
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


class Lines(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.selected_cell = None

    def render(self):
        colors = [pygame.Color(0, 0, 255), pygame.Color(255, 0, 0)]
        for i in range(self.width):
            for j in range(self.height):
                if self.board[j][i] == 1:
                    pygame.draw.ellipse(screen, colors[0], (self.left + i * self.cell_size, self.top +
                                                            j * self.cell_size, self.cell_size, self.cell_size), 0)
                elif self.board[j][i] == -1:
                    pygame.draw.ellipse(screen, colors[1], (self.left + i * self.cell_size, self.top +
                                                            j * self.cell_size, self.cell_size, self.cell_size), 0)

                pygame.draw.rect(screen, pygame.Color(125, 255, 255),
                                 (i * self.cell_size + self.left, j * self.cell_size + self.top, self.cell_size,
                                  self.cell_size), 1)

    # изменяет клетку
    def on_click(self, cell):
        if self.board[cell[1]][cell[0]] == 0:
            self.board[cell[1]][cell[0]] = 1
        elif self.board[cell[1]][cell[0]] == 1:
            self.board[cell[1]][cell[0]] = -1
        else:
            self.board[cell[1]][cell[0]] = 1







# поле 10 на 10
board = Lines(10, 10)
board.set_view(10, 10, 40)
running = True

while running:
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((72, 91, 73))
    board.render()
    pygame.display.flip()

pygame.quit()
