import pygame
import math
pygame.init()
size = width, height = 201, 201
a = 35 / 360
speed = 0  # скорость вращения
screen = pygame.display.set_mode(size)
# метод clock.tick() возвращает количество миллисекунд, прошедших с момента последнего вызова
clock = pygame.time.Clock()


def draw(a):
    pygame.draw.circle(screen, (255, 255, 255), (100, 100), 10)
    pygame.draw.polygon(screen,
                        (255, 255, 255), [(100, 100),
                                          (100 + 70 * math.cos(a * 3.14), 100 + 70 * math.sin(a * 3.14)),
                                          (100 + 70 * math.cos((a + 1/6) * 3.14), 100 + 70 * math.sin((a + 1/6) * 3.14))])

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # реакция на нажатие мыши
    if event.type == pygame.MOUSEBUTTONDOWN:
        pressed = pygame.mouse.get_pressed()
        # изменяем скорость в нужную сторону
        if event.button == 3:
            speed += 2 / 180
        elif event.button == 1:
            speed -= 2 / 180
    draw(a)
    a += speed
    pygame.display.flip()

    clock.tick(50)
pygame.quit()
