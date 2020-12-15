import pygame

def main():
    pygame.init()
    pygame.display.set_caption('Спрайты')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)

    running = True
    clock = pygame.time.Clock()
    while running:
        screen.fill(pygame.Color('white'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick()
    pygame.quit()

if __name__ == '__main__':
    main()