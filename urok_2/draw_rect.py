import pygame

size = width, height = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True

# Создаем второй холст
screen2 = pygame.Surface(screen.get_size())
x1, y1 = 0, 0
drawing = False  # режим рисования выключен
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True  # включаем режим рисования
            # Запоминаем координаты одного угла
            x1, y1 = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            # Сохраняем нарисованное (на втором холсте)
            screen2.blit(screen, (0, 0))
            drawing = False
        if event.type == pygame.MOUSEMOTION:
            # Запоминаем текущие размеры
            w, h = event.pos[0] - x1, event.pos[1] - y1
    # Рисуем на экране сохраненное на втором холсте
    screen.fill(pygame.Color('black'))
    screen.blit(screen2, (0, 0))
    if drawing:  # и, если надо, текущий прямоугольник
        pygame.draw.rect(screen, (0, 0, 255), ((x1, y1), (w, h)), 5)
    pygame.display.flip()
pygame.quit()