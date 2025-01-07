import pygame

if __name__ == '__main__':
    pygame.init()

    info = pygame.display.Info()
    width, height = info.current_w, info.current_h

    screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
    pygame.display.set_caption("game")

    running = True

    background_image = pygame.image.load("data/mainmenu.png")
    background_image = pygame.transform.scale(background_image, (width, height))

    button_text = "Играть"
    font = pygame.font.Font(None, 74)
    text_surface = font.render(button_text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(width // 2, height // 2))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        screen.blit(background_image, (0, 0))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
