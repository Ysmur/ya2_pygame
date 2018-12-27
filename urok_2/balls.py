import pygame
# инициализация Pygame:
pygame.init()
# размеры окна:
size = width, height = 800, 600
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
# clock.tick() возвращает количество миллисекунд, прошедших с момента последнего вызова
clock = pygame.time.Clock()

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
                pygame.draw.circle(screen, (255, 255, 255), event.pos, 20)


    # отрисовка и изменение свойств объектов


    # обновление экрана
    pygame.display.flip()