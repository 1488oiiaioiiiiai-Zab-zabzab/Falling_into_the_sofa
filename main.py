import pygame
import sys
import sqlite3
import os

FPS = 60
CURRENTSAVESLOT = 0


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

    global CURRENTSAVESLOT

    if len(getalldatafromsaveslot(1)) == 0:
        slotbtn1_text = "Слот1"
    else:
        slotbtn1_text = getalldatafromsaveslot(1)[0][1]
    x = (width - button_width) // 4
    y = height // 2 + (1 - 1.5) * button_height
    button1 = pygame.Rect(x, y, button_width, button_height)

    if len(getalldatafromsaveslot(2)) == 0:
        slotbtn2_text = "Слот2"
    else:
        slotbtn2_text = getalldatafromsaveslot(2)[0][1]
        print(slotbtn2_text)
    x2 = (width - button_width) // 2
    y2 = height // 2 + (1 - 1.5) * button_height
    button2 = pygame.Rect(x2, y2, button_width, button_height)

    if len(getalldatafromsaveslot(3)) == 0:
        slotbtn3_text = "Слот3"
    else:
        slotbtn3_text = getalldatafromsaveslot(3)[0][1]
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
                    CURRENTSAVESLOT = 1
                    return
                elif delete_button1.collidepoint(event.pos) and buttonpressed == 1:
                    con = sqlite3.connect("gamedata.db")

                    cur = con.cursor()

                    pon = """DELETE FROM saveslotsdata WHERE slot_number = 1"""
                    cur.execute(pon)

                    con.commit()
                    con.close()
                    slotbtn1_text = "Слот1"
                elif play_button2.collidepoint(event.pos) and buttonpressed == 2:
                    CURRENTSAVESLOT = 2
                    return
                elif delete_button2.collidepoint(event.pos) and buttonpressed == 2:
                    con = sqlite3.connect("gamedata.db")

                    cur = con.cursor()

                    pon = """DELETE FROM saveslotsdata WHERE slot_number = 2"""
                    cur.execute(pon)

                    con.commit()
                    con.close()
                    slotbtn2_text = "Слот2"
                elif play_button3.collidepoint(event.pos) and buttonpressed == 3:
                    CURRENTSAVESLOT = 3
                    return
                elif delete_button3.collidepoint(event.pos) and buttonpressed == 3:
                    con = sqlite3.connect("gamedata.db")

                    cur = con.cursor()

                    pon = """DELETE FROM saveslotsdata WHERE slot_number = 3"""
                    cur.execute(pon)

                    con.commit()
                    con.close()
                    slotbtn3_text = "Слот3"
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
            pygame.draw.rect(screen, (231, 76, 60), delete_button1)

            skibidifont = pygame.font.Font(None, 15)
            play_text_surface = font.render("Играть", True, (0, 0, 0))
            delete_text_surface = skibidifont.render("Удалить сохранение", True, (0, 0, 0))

            play_text_rect = play_text_surface.get_rect(center=play_button1.center)
            delete_text_rect = delete_text_surface.get_rect(center=delete_button1.center)

            screen.blit(play_text_surface, play_text_rect)
            screen.blit(delete_text_surface, delete_text_rect)
        elif buttonpressed == 2:
            pygame.draw.rect(screen, (192, 192, 192), play_button2)
            pygame.draw.rect(screen, (231, 76, 60), delete_button2)

            skibidifont = pygame.font.Font(None, 15)
            play_text_surface = font.render("Играть", True, (0, 0, 0))
            delete_text_surface = skibidifont.render("Удалить сохранение", True, (0, 0, 0))

            play_text_rect = play_text_surface.get_rect(center=play_button2.center)
            delete_text_rect = delete_text_surface.get_rect(center=delete_button2.center)

            screen.blit(play_text_surface, play_text_rect)
            screen.blit(delete_text_surface, delete_text_rect)

        elif buttonpressed == 3:
            pygame.draw.rect(screen, (192, 192, 192), play_button3)
            pygame.draw.rect(screen, (231, 76, 60), delete_button3)

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


class MusicBox(pygame.sprite.Sprite):
    def __init__(self, music, pos_x, pos_y):
        super().__init__(all_sprites, enter_box)
        self.played = False
        self.music = music
        self.image1 = load_image("empty.png")
        self.image = pygame.transform.scale(self.image1, (tile_width, tile_height))
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)

    def event(self):
        if not self.played:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(self.music)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.3)
            self.played = True


class Checkpoint(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, name):
        super().__init__(all_sprites, checkpoint_group)
        self.x = pos_x
        self.y = pos_y
        self.name = name
        self.image1 = load_image("checkpoint.png")
        self.image = pygame.transform.scale(self.image1, (tile_width * 2, 2 * tile_height))
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)

    def interact(self):
        a = getalldatafromsaveslot(CURRENTSAVESLOT)
        if len(a) == 0:
            con = sqlite3.connect("gamedata.db")
            cur = con.cursor()

            cur.execute("""INSERT INTO saveslotsdata (slot_number, name, checkpoint_x, checkpoint_y) 
                                          VALUES (?, ?, ?, ?)""",
                        (CURRENTSAVESLOT, self.name, self.x, self.y))

            con.commit()
            con.close()
        else:
            con = sqlite3.connect("gamedata.db")
            cur = con.cursor()

            cur.execute("""UPDATE saveslotsdata 
                           SET name = ?, checkpoint_x = ?, checkpoint_y = ? 
                           WHERE slot_number = ?""",
                        (self.name, self.x, self.y, CURRENTSAVESLOT))

            con.commit()
            con.close()


class TrainingDummy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, enemy_group)
        self.image1 = load_image("enemies/training_dummy/dummy.png")
        self.image = pygame.transform.scale(self.image1, (player_width, player_height))
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)
        self.health = 1000
        self.killed = False
        self.hurt_frame_index = 0
        self.hurt_frame_counter = 0
        self.hurt_frame_delay = 5
        self.is_hurt = False
        self.hurt_images = [pygame.transform.scale(load_image("enemies/training_dummy/damageddummysprite.png"),
                                                   (player_width, player_height)),
                            pygame.transform.scale(load_image("enemies/training_dummy/damageddummysprite.png"),
                                                   (player_width, player_height))
                            ]

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.killed = True
            print(1)
        else:
            self.is_hurt = True

    def update(self):
        if self.killed:
            self.image = load_image("enemies/training_dummy/deaddummysprite.png")
        elif self.is_hurt:
            self.animate_hurt()
        else:
            self.image = pygame.transform.scale(self.image1, (player_width, player_height))

    def animate_hurt(self):
        self.hurt_frame_counter += 1
        if self.hurt_frame_counter >= self.hurt_frame_delay:
            self.hurt_frame_counter = 0
            self.hurt_frame_index += 1

            if self.hurt_frame_index < len(self.hurt_images):
                self.image = self.hurt_images[self.hurt_frame_index]
            else:
                self.hurt_frame_index = 0
                self.is_hurt = False


class Walkingsoul(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, enemy_group, melee_enemy_group, enter_box)
        self.image1 = load_image("enemies/walkingsoul/soulwalkl1.png")
        self.image = pygame.transform.scale(self.image1, (player_width, player_height))
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)
        self.health = 1000
        self.killed = False
        self.hurt_frame_index = 0
        self.hurt_frame_counter = 0
        self.hurt_frame_delay = 5
        self.is_hurt = False
        self.hurt_images = [pygame.transform.scale(load_image("enemies/walkingsoul/soulgetdmg.png"),
                                                   (player_width, player_height)),
                            pygame.transform.scale(load_image("enemies/walkingsoul/soulgetdmg.png"),
                                                   (player_width, player_height))
                            ]
        self.frame_index = 0
        self.frame_delay = 10
        self.frame_counter = 0
        self.stand_frames = [pygame.transform.scale(load_image("enemies/walkingsoul/soulwalkl1.png"),
                                                    (player_width, player_height)),
                             pygame.transform.scale(load_image("enemies/walkingsoul/soulwalkl2.png"),
                                                    (player_width, player_height))]
        self.direction = 1

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.killed = True
            print(1)
        else:
            self.is_hurt = True

    def update(self):
        if self.killed:
            self.image = pygame.transform.scale(load_image("empty.png"),
                                                (player_width, player_height))
        elif self.is_hurt:
            self.animate_hurt()
        else:
            self.animate_standing()

    def animate_hurt(self):
        self.hurt_frame_counter += 1
        if self.hurt_frame_counter >= self.hurt_frame_delay:
            self.hurt_frame_counter = 0
            self.hurt_frame_index += 1

            if self.hurt_frame_index < len(self.hurt_images):
                self.image = self.hurt_images[self.hurt_frame_index]
            else:
                self.hurt_frame_index = 0
                self.is_hurt = False

    def animate_standing(self):
        self.frame_counter += 1
        if self.frame_counter >= self.frame_delay:
            self.frame_counter = 0
            self.frame_index = (self.frame_index + 1) % len(self.stand_frames)
            self.current_frame = self.stand_frames[self.frame_index]
            if self.direction == -1:
                self.image = pygame.transform.flip(self.current_frame, True, False)
            else:
                self.image = self.current_frame

    def event(self):
        pass


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image1 = player_image
        self.image = pygame.transform.scale(self.image1, (player_width, player_height))
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)
        self.frame_index = 0
        self.frame_delay = 10
        self.frame_counter = 0
        self.gravity = 0.5
        self.velocity_y = 0
        self.on_ground = False
        self.is_move = False
        self.stand_frames = [
            pygame.transform.scale(load_image("player/idle_animation/charakterspriteanimationidle1.png"),
                                   (player_width, player_height)),
            pygame.transform.scale(load_image("player/idle_animation/charakterspriteanimationidle2.png"),
                                   (player_width, player_height)),
            pygame.transform.scale(load_image("player/idle_animation/charakterspriteanimationidle3.png"),
                                   (player_width, player_height)),
            pygame.transform.scale(load_image("player/idle_animation/charakterspriteanimationidle4.png"),
                                   (player_width, player_height))]
        self.run_frames = [pygame.transform.scale(load_image("player/run_animation/charakterspriteanimationrun1.png"),
                                                  (player_width, player_height)),
                           pygame.transform.scale(load_image("player/run_animation/charakterspriteanimationrun2.png"),
                                                  (player_width, player_height)),
                           pygame.transform.scale(load_image("player/run_animation/charakterspriteanimationrun3.png"),
                                                  (player_width, player_height)),
                           pygame.transform.scale(load_image("player/run_animation/charakterspriteanimationrun4.png"),
                                                  (player_width, player_height)),
                           pygame.transform.scale(load_image("player/run_animation/charakterspriteanimationrun5.png"),
                                                  (player_width, player_height)),
                           pygame.transform.scale(load_image("player/run_animation/charakterspriteanimationrun6.png"),
                                                  (player_width, player_height))
                           ]
        self.jump_frames = [pygame.transform.scale(load_image("player/jumpanimation/charakterspritefalling.png"),
                                                   (player_width, player_height)),
                            pygame.transform.scale(load_image("player/jumpanimation/charakterspritejump.png"),
                                                   (player_width, player_height))]
        self.stand_index = 0
        self.stand_delay = 10
        self.stand_counter = 0
        self.direction = 1

        self.attack_frames = [pygame.transform.scale(load_image("player/atk_animation/charakterspriteatkanim1.png"),
                                                     (player_width, player_height)),
                              pygame.transform.scale(load_image("player/atk_animation/charakterspriteatkanim2.png"),
                                                     (player_width, player_height)),
                              pygame.transform.scale(load_image("player/atk_animation/charakterspriteatkanim3.png"),
                                                     (player_width, player_height))]
        self.is_attacking = False
        self.attack_frame_index = 0
        self.attack_frame_counter = 0
        self.attack_frame_delay = 5

    def move(self, dx, dy, tiles):
        if dx < 0:
            self.direction = -1
        elif dx > 0:
            self.direction = 1

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

    def update(self, boxes):
        if self.is_attacking:
            self.animate_attack()
        elif self.on_ground and not self.is_move:
            self.animate_standing()
        elif not self.on_ground:
            if self.direction == -1:
                self.image = pygame.transform.flip(self.jump_frames[1], True, False)
            else:
                self.image = self.jump_frames[1]
        elif self.is_move:
            self.animate_running()

        for i in boxes:
            if self.rect.colliderect(i.rect):
                i.event()

    def animate_standing(self):
        self.frame_counter += 1
        if self.frame_counter >= self.frame_delay:
            self.frame_counter = 0
            self.frame_index = (self.frame_index + 1) % len(self.stand_frames)
            self.current_frame = self.stand_frames[self.frame_index]
            if self.direction == -1:
                self.image = pygame.transform.flip(self.current_frame, True, False)
            else:
                self.image = self.current_frame

    def animate_running(self):
        self.frame_counter += 1
        if self.frame_counter >= self.frame_delay:
            self.frame_counter = 0
            self.frame_index = (self.frame_index + 1) % len(self.run_frames)
            self.current_frame = self.run_frames[self.frame_index]
            if self.direction == -1:
                self.image = pygame.transform.flip(self.current_frame, True, False)
            else:
                self.image = self.current_frame

    def interact(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_mask(self, sprite):
                sprite.interact()

    def m1atk(self):
        if not self.is_attacking:
            self.is_attacking = True
            self.attack_frame_index = 0

    def animate_attack(self):
        self.attack_frame_counter += 1
        if self.attack_frame_counter >= self.attack_frame_delay:
            self.attack_frame_counter = 0
            self.attack_frame_index += 1
            if self.attack_frame_index >= len(self.attack_frames):
                self.is_attacking = False
                self.attack_frame_index = 0
            else:
                if self.direction == -1:
                    self.image = pygame.transform.flip(self.attack_frames[self.attack_frame_index], True, False)
                else:
                    self.image = self.attack_frames[self.attack_frame_index]

        if self.is_attacking:
            if self.direction == -1:
                hitbox_position = (self.rect.x, self.rect.y)
                hitbox_size = (40, 20)
            else:
                hitbox_position = (self.rect.x + (player_width // 3) * 3, self.rect.y)
                hitbox_size = (40, 20)
            self.damage_box(hitbox_position, hitbox_size)

    def damage_box(self, position, size):
        hitbox = pygame.Rect(position, size)
        for enemy in enemy_group:
            if hitbox.colliderect(enemy.rect):
                enemy.take_damage(10)


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


def generate_level(level):
    new_player, x, y = None, None, None
    enemies = []
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                pass
            elif level[y][x] == '#':
                Tile('floor', x, y)
            elif level[y][x] == "T":
                Tile("towerrock", x, y)
            elif level[y][x] == "=":
                enemies.append(TrainingDummy(x, y))
            elif level[y][x] == "$":
                enemies.append(Walkingsoul(x, y))
            elif level[y][x] == '@':
                con = sqlite3.connect("gamedata.db")

                cur = con.cursor()

                x1 = f"""SELECT checkpoint_x FROM saveslotsdata 
                    WHERE slot_number = {CURRENTSAVESLOT}"""
                x1 = cur.execute(x1).fetchone()

                y1 = f"""SELECT checkpoint_y FROM saveslotsdata 
                                    WHERE slot_number = {CURRENTSAVESLOT}"""
                y1 = cur.execute(y1).fetchone()

                con.close()

                if y1 and x1:
                    new_player = Player(x1[0], y1[0])
                else:
                    new_player = Player(x, y)
            elif level[y][x] == "1":
                Checkpoint(x, y, "тренеровка")
            elif level[y][x] == "2":
                Checkpoint(x, y, "вход в башню")
    MusicBox("data/music/Destroyed Realities - EXISTENTIA (Arrangement).mp3", 167, 15)
    return new_player, x, y, enemies


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    info = pygame.display.Info()
    width, height = info.current_w, info.current_h
    screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
    pygame.display.set_caption("game")

    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    checkpoint_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    melee_enemy_group = pygame.sprite.Group()
    enter_box = pygame.sprite.Group()

    start_screen()
    saveslots()
    pygame.mouse.set_visible(False)

    tile_width = tile_height = (height + width) // 64

    tile_images = {'floor': load_image("tiles/floor.png"), "towerrock": load_image("tiles/towerrock.png")}

    player_width = player_height = (height + width) // 16

    player_image = load_image('player/maincharacter.png')

    camera = Camera()

    player, level_x, level_y, enemies = generate_level(load_level('map1.txt'))
    running = True
    player_speed = 10
    clock = pygame.time.Clock()

    pygame.mixer.music.load("data/music/𝘾𝙃𝙀𝙎𝙎 𝙏𝙔𝙋𝙀 𝘽𝙀𝘼𝙏 (𝙎𝙇𝙊𝙒𝙀𝘿).mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.m1atk()
            if event.type == pygame.KEYDOWN:
                a = pygame.key.get_pressed()
                if a[pygame.K_ESCAPE]:
                    terminate()
                if a[pygame.K_e]:
                    player.interact(checkpoint_group)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.is_move = True
            player.move(-player_speed, 0, tiles_group)
        elif keys[pygame.K_d]:
            player.is_move = True
            player.move(player_speed, 0, tiles_group)
        else:
            player.is_move = False
        if keys[pygame.K_SPACE]:
            player.jump()

        player.power_of_gravity(tiles_group)
        player.update(enter_box)
        camera.update(player)

        for i in enemies:
            i.update()

        for sprite in all_sprites:
            camera.apply(sprite)
        screen.fill(pygame.Color((50, 39, 30)))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
