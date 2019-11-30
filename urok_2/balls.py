import pygame
# инициализация Pygame:
pygame.init()
# размеры окна:
size = width, height = 400, 400
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
# clock.tick() возвращает количество миллисекунд, прошедших с момента последнего вызова
clock = pygame.time.Clock()

x = -10
y = -10
speed = [0, 0]

# основной цикл
running = True
while running:
    # внутри игрового цикла ещё один цикл
    # приема и обработки сообщений
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                screen.fill((0, 0, 0))
                x, y = event.pos
                speed = [1, -1]


    # отрисовка и изменение свойств объектов
    if x >= width or x <= 0:
        speed[0] = - speed[0]
    x += speed[0]
    if y >= height or y <= 0:
        speed[1] = - speed[1]
    y += speed[1]
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 10)


    # обновление экрана
    pygame.display.flip()
    clock.tick(100)