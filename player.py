import pygame

import game
from spritesheet import Spritesheet


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = Spritesheet('assets/sheet_law.png')

        self.images = []
        self.images.append(self.sprite_sheet.get_sprite(0, 0, 56, 84))
        self.images.append(self.sprite_sheet.get_sprite(0, 84, 54, 84))
        self.images.append(self.sprite_sheet.get_sprite(115, 84, 54, 84))
        self.images.append(self.sprite_sheet.get_sprite(168, 84, 54, 84))
        self.images.append(self.sprite_sheet.get_sprite(222, 84, 54, 84))
        self.images.append(self.sprite_sheet.get_sprite(276, 84, 54, 84))
        self.images.append(self.sprite_sheet.get_sprite(330, 84, 54, 84))
        self.images.append(self.sprite_sheet.get_sprite(384, 84, 54, 84))
        self.is_animating = False

        self.current_sprite = 0
        self.image = self.images[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.velocity = [0, 0]
        self.speed = 5
        self.jump_force = 3
        self.is_jumping = False

    def move(self):
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def animate(self):
        self.is_animating = True
        self.update()

    def check_collision(self):
        if self.rect.colliderect(game.Game(None).left_wall):
            self.rect.x += 0.01
            self.velocity[0] = 0
        elif self.rect.colliderect(game.Game(None).right_wall):
            self.rect.x -= 0.01
            self.velocity[0] = 0
        else:
            self.move()

    def update(self):
        if self.is_animating is True:
            self.current_sprite += 0.1

        if self.current_sprite >= len(self.images):
            self.current_sprite = 2

        self.image = self.images[int(self.current_sprite)]

    def jump(self, event):
        if event.type == pygame.KEYDOWN and self.is_jumping is True:
            if event.key == pygame.K_SPACE:
                self.velocity[1] = -self.jump_force
                self.is_jumping = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
