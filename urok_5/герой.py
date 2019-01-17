import pygame
import os


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

hero_image = load_image("creature.png")

hero = pygame.sprite.Sprite(all_sprites)
hero.image = hero_image
hero.rect = hero.image.get_rect()
all_sprites.add(hero)

running = True
while running:
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            hero.rect.top += 10
        elif key[pygame.K_UP]:
            hero.rect.top -= 10
        if key[pygame.K_RIGHT]:
            hero.rect.left += 10
        elif key[pygame.K_LEFT]:
            hero.rect.left -= 10
    screen.fill((0, 0, 78))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
