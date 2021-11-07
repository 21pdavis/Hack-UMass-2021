import pygame
import sys


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        # list for boot-up animation
        self.attack_animation = False
        self.bootup_sprites = []
        self.bootup_sprites.append(pygame.image.load('face_1.png'))
        self.bootup_sprites.append(pygame.image.load('face_2.png'))
        self.bootup_sprites.append(pygame.image.load('face_3.png'))
        self.bootup_sprites.append(pygame.image.load('face_4.png'))
        self.bootup_sprites.append(pygame.image.load('face_5.png'))
        self.bootup_sprites.append(pygame.image.load('face_6.png'))
        self.bootup_sprites.append(pygame.image.load('face_7.png'))

        # list for wink animation
        self.wink_animation = False
        self.wink_sprites = []
        self.wink_sprites.append(pygame.image.load('face_5.png'))
        self.wink_sprites.append(pygame.image.load('face_8.png'))
        self.wink_sprites.append(pygame.image.load('face_9.png'))
        self.wink_sprites.append(pygame.image.load('face_8.png'))
        self.wink_sprites.append(pygame.image.load('face_5.png'))

        self.current_sprite = 4
        self.image = self.bootup_sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        #self.rect.topleft = [pos_x, pos_y]
        self.rect.center = (325, 200)

    def attack(self):
        self.current_sprite = 0
        if not self.wink_animation:
            self.attack_animation = True

    def wink(self):
        self.current_sprite = 0
        if not self.attack_animation:
            self.wink_animation = True

    def update(self, speed):
        # boot up smile
        if self.attack_animation:
            print(str(self.current_sprite)+" | speed = "+str(speed))
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.bootup_sprites):
                self.current_sprite = 4
                self.attack_animation = False
        # wink animation
        if self.wink_animation:
            print(str(self.current_sprite) + " | speed = " + str(speed))
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.wink_sprites):
                self.current_sprite = 4
                self.wink_animation = False

        self.image = self.wink_sprites[int(self.current_sprite)]


# General setup
# pygame.init()
# clock = pygame.time.Clock()

# # Game Screen
# os.environ["DISPLAY"] = ":0"
# pygame.display.init()
# screen_width = 800
# screen_height = 480
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Sprite Animation")

# # Creating the sprites and groups
# moving_sprites = pygame.sprite.Group()
# player = Player(100, 100)
# moving_sprites.add(player)

# # while True:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             pygame.quit()
# #             sys.exit()
#         if event.type == pygame.KEYDOWN:
#             player.attack()

#     # Drawing
#     screen.fill((0, 0, 0))
#     moving_sprites.draw(screen)
#     moving_sprites.update(0.035)
#     pygame.display.flip()
#     clock.tick(60)
