import os
import pygame

size = width, height = 600, 300
screen = pygame.display.set_mode(size)


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


class Gameover(pygame.sprite.Sprite):
    image = load_image("gameover.png")

    def __init__(self):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite
        super().__init__(all_sprites)
        self.image = Gameover.image
        self.rect = self.image.get_rect()
        self.rect.left = -600
        self.rect.top = -300

    def update(self):
        if self.rect.left < 0:
            self.rect.left += 4
            self.rect.top += 2


clock = pygame.time.Clock()

# группа, содержащая все спрайты
all_sprites = pygame.sprite.Group()
Gameover = Gameover()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(50)

pygame.quit()
