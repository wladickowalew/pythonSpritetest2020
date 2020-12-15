import os, sys, random
import pygame

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image



def main():
    pygame.init()
    pygame.display.set_caption('Спрайты')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)

    class Bomb(pygame.sprite.Sprite):
        image = load_image("bomb.png")
        def __init__(self, *group):
            super().__init__(*group)
            self.image = Bomb.image
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(height - self.rect.height)

        def update(self):
            self.rect = self.rect.move(random.randrange(3) - 1, 
                                       random.randrange(3) - 1)

    # создадим группу, содержащую все спрайты
    all_sprites = pygame.sprite.Group()

    for i in range(50):
        Bomb(all_sprites)

    running = True
    clock = pygame.time.Clock()
    while running:
        screen.fill(pygame.Color('white'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__ == '__main__':
    main()

