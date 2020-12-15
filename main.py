import os, sys
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

    # создадим группу, содержащую все спрайты
    all_sprites = pygame.sprite.Group()

    # создадим спрайт
    sprite = pygame.sprite.Sprite()
    # определим его вид
    sprite.image = load_image("bomb.png")
    # и размеры
    sprite.rect = sprite.image.get_rect()
    # добавим спрайт в группу
    sprite.rect.x = 5
    sprite.rect.y = 20
    all_sprites.add(sprite)

    running = True
    clock = pygame.time.Clock()
    while running:
        screen.fill(pygame.Color('white'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.draw(screen)            
        pygame.display.flip()
        clock.tick()
    pygame.quit()

if __name__ == '__main__':
    main()
