import pygame
import os
import random


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


pygame.init()
size = width, height = 501, 501
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()

cursor_image = load_image("arrow.png")

cursor = pygame.sprite.Sprite(all_sprites)
cursor.image = cursor_image
cursor.rect = cursor.image.get_rect()
all_sprites.add(cursor)

# скрываем системный курсор
pygame.mouse.set_visible(False)
running = True

while running:
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            cursor.rect.x = event.pos[0]
            cursor.rect.y = event.pos[1]
    screen.fill((0, 0, 78))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
