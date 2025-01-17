import pygame
import sys
import sqlite3
import os

FPS = 60


def getalldatafromsaveslot(slotnumber):
    con = sqlite3.connect("gamedata.db")

    cur = con.cursor()

    pon = f"""SELECT * FROM saveslotsdata 
        WHERE slot_number = {int(slotnumber)}"""
    result = cur.execute(pon).fetchall()

    con.close()

    return result


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

    button_width = 200
    button_height = 50

    buttonpressed = 0

    if len(getalldatafromsaveslot(1)) == 0:
        slotbtn1_text = "Слот1"
    else:
        slotbtn1_text = getalldatafromsaveslot(1)[1]
    x = (width - button_width) // 4
    y = height // 2 + (1 - 1.5) * button_height
    button1 = pygame.Rect(x, y, button_width, button_height)

    if len(getalldatafromsaveslot(2)) == 0:
        slotbtn2_text = "Слот2"
    else:
        slotbtn2_text = getalldatafromsaveslot(1)[1]
    x2 = (width - button_width) // 2
    y2 = height // 2 + (1 - 1.5) * button_height
    button2 = pygame.Rect(x2, y2, button_width, button_height)

    if len(getalldatafromsaveslot(3)) == 0:
        slotbtn3_text = "Слот3"
    else:
        slotbtn3_text = getalldatafromsaveslot(1)[1]
    x3 = (width - button_width) // 1.25
    y3 = height // 2 + (1 - 1.5) * button_height
    button3 = pygame.Rect(x3, y3, button_width, button_height)

    play_button1 = pygame.Rect(button1.x, button1.y + button_height + 10, button_width, button_height)
    delete_button1 = pygame.Rect(button1.x, button1.y + 2 * button_height + 20, button_width, button_height)

    play_button2 = pygame.Rect(button2.x, button1.y + button_height + 10, button_width, button_height)
    delete_button2 = pygame.Rect(button2.x, button1.y + 2 * button_height + 20, button_width, button_height)

    play_button3 = pygame.Rect(button3.x, button3.y + button_height + 10, button_width, button_height)
    delete_button3 = pygame.Rect(button3.x, button3.y + 2 * button_height + 20, button_width, button_height)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                a = pygame.key.get_pressed()
                if a[pygame.K_ESCAPE]:
                    terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    buttonpressed = 1
                elif button2.collidepoint(event.pos):
                    buttonpressed = 2
                elif button3.collidepoint(event.pos):
                    buttonpressed = 3
                elif play_button1.collidepoint(event.pos) and buttonpressed == 1:
                    return
                elif delete_button1.collidepoint(event.pos) and buttonpressed == 1:
                    print("Удалить сохранение нажато")
                elif play_button2.collidepoint(event.pos) and buttonpressed == 2:
                    return
                elif delete_button2.collidepoint(event.pos) and buttonpressed == 2:
                    print("Удалить сохранение нажато")
                elif play_button3.collidepoint(event.pos) and buttonpressed == 3:
                    return
                elif delete_button3.collidepoint(event.pos) and buttonpressed == 3:
                    print("Удалить сохранение нажато")
                else:
                    buttonpressed = 0

        screen.blit(background_image, (0, 0))
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
        if buttonpressed == 1:
            pygame.draw.rect(screen, (192, 192, 192), play_button1)
            pygame.draw.rect(screen, (192, 192, 192), delete_button1)

            skibidifont = pygame.font.Font(None, 15)
            play_text_surface = font.render("Играть", True, (0, 0, 0))
            delete_text_surface = skibidifont.render("Удалить сохранение", True, (0, 0, 0))

            play_text_rect = play_text_surface.get_rect(center=play_button1.center)
            delete_text_rect = delete_text_surface.get_rect(center=delete_button1.center)

            screen.blit(play_text_surface, play_text_rect)
            screen.blit(delete_text_surface, delete_text_rect)
        elif buttonpressed == 2:
            pygame.draw.rect(screen, (192, 192, 192), play_button2)
            pygame.draw.rect(screen, (192, 192, 192), delete_button2)

            skibidifont = pygame.font.Font(None, 15)
            play_text_surface = font.render("Играть", True, (0, 0, 0))
            delete_text_surface = skibidifont.render("Удалить сохранение", True, (0, 0, 0))

            play_text_rect = play_text_surface.get_rect(center=play_button2.center)
            delete_text_rect = delete_text_surface.get_rect(center=delete_button2.center)

            screen.blit(play_text_surface, play_text_rect)
            screen.blit(delete_text_surface, delete_text_rect)

        elif buttonpressed == 3:
            pygame.draw.rect(screen, (192, 192, 192), play_button3)
            pygame.draw.rect(screen, (192, 192, 192), delete_button3)

            skibidifont = pygame.font.Font(None, 15)
            play_text_surface = font.render("Играть", True, (0, 0, 0))
            delete_text_surface = skibidifont.render("Удалить сохранение", True, (0, 0, 0))

            play_text_rect = play_text_surface.get_rect(center=play_button3.center)
            delete_text_rect = delete_text_surface.get_rect(center=delete_button3.center)

            screen.blit(play_text_surface, play_text_rect)
            screen.blit(delete_text_surface, delete_text_rect)

        pygame.display.flip()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
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


def load_level(filename):
    filename = "maps/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image1 = tile_images[tile_type]
        self.image = pygame.transform.scale(self.image1, (tile_width, tile_height))
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image1 = player_image
        self.image = pygame.transform.scale(self.image1, (player_width, player_height))
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)
        self.gravity = 0.5
        self.velocity_y = 0
        self.on_ground = False

    def move(self, dx, dy, tiles):
        old_rect = self.rect.copy()

        self.rect.x += dx
        for tile in tiles:
            if pygame.sprite.collide_mask(self, tile) or self.rect.x < -200:
                self.rect.x = old_rect.x
                break

    def jump(self):
        if self.on_ground:
            self.velocity_y = -10

    def power_of_gravity(self, tiles):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y
        old_rect = self.rect.copy()

        self.on_ground = False
        for tile in tiles:
            if pygame.sprite.collide_mask(self, tile):
                if self.velocity_y > 0:
                    self.rect.bottom = tile.rect.top
                    self.on_ground = True
                    self.velocity_y = 0
                else:
                    self.rect.y = old_rect.y
        if not self.on_ground:
            self.rect.y += self.velocity_y


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                pass
            elif level[y][x] == '#':
                Tile('floor', x, y)
            elif level[y][x] == '@':
                new_player = Player(x, y)
    return new_player, x, y


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    pygame.init()
    info = pygame.display.Info()
    width, height = info.current_w, info.current_h
    screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
    pygame.display.set_caption("game")

    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()

    start_screen()
    saveslots()

    tile_width = tile_height = (height + width) // 64

    tile_images = {'floor': load_image("tiles/floor.png")}

    player_width = player_height = (height + width) // 16

    player_image = load_image('player/maincharacter.png')

    player, level_x, level_y = generate_level(load_level('map1.txt'))
    running = True
    player_speed = 10
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                a = pygame.key.get_pressed()
                if a[pygame.K_ESCAPE]:
                    terminate()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.move(-player_speed, 0, tiles_group)
        if keys[pygame.K_d]:
            player.move(player_speed, 0, tiles_group)
        if keys[pygame.K_SPACE]:
            player.jump()
        player.power_of_gravity(tiles_group)

        screen.fill(pygame.Color((7, 18, 30)))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
