import pygame
import sys
import sqlite3

FPS = 60

pygame.init()
info = pygame.display.Info()
width, height = info.current_w, info.current_h

screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
pygame.display.set_caption("game")


def start_screen():
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
                terminate()
            if event.type == pygame.KEYDOWN:
                a = pygame.key.get_pressed()
                if a[pygame.K_ESCAPE]:
                    terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_rect.collidepoint(event.pos):
                    return
        screen.fill((0, 0, 0))
        screen.blit(background_image, (0, 0))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()


def saveslots():
    running = True

    background_image = pygame.image.load("data/mainmenu.png")
    background_image = pygame.transform.scale(background_image, (width, height))
    screen.blit(background_image, (0, 0))

    button_width = 200
    button_height = 50

    slotbtn1_text = "Слот1"
    x = (width - button_width) // 4
    y = height // 2 + (1 - 1.5) * button_height
    button1 = pygame.Rect(x, y, button_width, button_height)

    slotbtn2_text = "Слот2"
    x2 = (width - button_width) // 2
    y2 = height // 2 + (1 - 1.5) * button_height
    button2 = pygame.Rect(x2, y2, button_width, button_height)

    slotbtn3_text = "Слот3"
    x3 = (width - button_width) // 1.25
    y3 = height // 2 + (1 - 1.5) * button_height
    button3 = pygame.Rect(x3, y3, button_width, button_height)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                a = pygame.key.get_pressed()
                if a[pygame.K_ESCAPE]:
                    terminate()

        pygame.draw.rect(screen, (192, 192, 192), button1)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(slotbtn1_text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=button1.center)
        screen.blit(text_surface, text_rect)

        pygame.draw.rect(screen, (192, 192, 192), button2)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(slotbtn2_text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=button2.center)
        screen.blit(text_surface, text_rect)

        pygame.draw.rect(screen, (192, 192, 192), button3)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(slotbtn3_text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=button3.center)
        screen.blit(text_surface, text_rect)

        pygame.display.flip()


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    start_screen()
    saveslots()
