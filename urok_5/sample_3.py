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
# изображение должно лежать в папке data
bomb_image = load_image("bomb.png")

for i in range(50):
    # можно сразу создавать спрайты с указанием группы
    bomb = pygame.sprite.Sprite(all_sprites)
    bomb.image = bomb_image
    bomb.rect = bomb.image.get_rect()

    # задаём случайное местоположение бомбочке
    bomb.rect.x = random.randrange(width)
    bomb.rect.y = random.randrange(height)




running = True

while running:
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
    screen.fill((56, 45, 78))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
