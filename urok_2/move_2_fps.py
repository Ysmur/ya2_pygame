import pygame

size = width, height = 301, 301
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True
x_pos = 0
v = 20  # пикселей в секунду
fps = 60

while running:
    # внутри игрового цикл еще один цикл
    # приема и обработки сообщений
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False

    # отрисовка и изменение свойств объектов
    # ...
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (int(x_pos), 200), 20)
    x_pos += v / fps
    clock.tick(fps)

    # обновление экрана
    pygame.display.flip()

pygame.quit()