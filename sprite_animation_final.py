import pygame
import sys
import os


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        
        self.attack_animation = False
        self.sprites = []
        self.sprites.append(pygame.image.load('face_1.png'))
        self.sprites.append(pygame.image.load('face_2.png'))
        self.sprites.append(pygame.image.load('face_3.png'))
        self.sprites.append(pygame.image.load('face_4.png'))
        self.sprites.append(pygame.image.load('face_5.png'))
        self.sprites.append(pygame.image.load('face_6.png'))
        self.sprites.append(pygame.image.load('face_7.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        #self.rect.topleft = [pos_x, pos_y]
        self.rect.center = (400, 240)

    def attack(self):
        self.attack_animation = True

    def update(self, speed):
        if self.attack_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.attack_animation = False

        self.image = self.sprites[int(self.current_sprite)]


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
