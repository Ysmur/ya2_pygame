import os
import pygame

size = width, height = 51, 500
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

class Sprite(pygame.sprite.Sprite):
    image = load_image("sprite.jpg")

    def __init__(self, pos_x, pos_y):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite
        super().__init__(all_sprites)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = load_image("sprite.jpg")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.left = self.pos_x
        self.rect.top = self.pos_y

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            self.rect.left = self.pos_x + 1
            self.rect.top = self.pos_y

    def update(self):
        if self.rect.left > self.pos_x:
            self.rect.left += 1


clock = pygame.time.Clock()

# группа, содержащая все спрайты
all_sprites = pygame.sprite.Group()
Sprite_1 = Sprite(0, 0)
Sprite_2 = Sprite(0, 100)
Sprite_3 = Sprite(0, 200)
Sprite_4 = Sprite(0, 300)
Sprite_5 = Sprite(0, 400)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in all_sprites:
                sprite.get_event(event)
    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(50)

pygame.quit()
