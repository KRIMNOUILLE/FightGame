import pygame
from player import Player


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.bg = pygame.image.load('assets/arena.png')
        self.running = True
        self.player = Player(500, 500)
        self.gravity = 0.1
        self.clock = pygame.time.Clock()
        self.floor = pygame.Rect(0, 687, 1280, 33)
        self.left_wall = pygame.Rect(-30, 0, 30, 720)
        self.right_wall = pygame.Rect(1290, 0, 30, 720)

    def handling_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.player.jump(event)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.velocity[0] = -1
            self.player.image = pygame.transform.flip(self.player.image, True, False)
            self.player.animate()
        elif keys[pygame.K_RIGHT]:
            self.player.velocity[0] = 1
            self.player.animate()
        else:
            self.player.velocity[0] = 0
            self.player.current_sprite = 0
            self.player.image = self.player.images[self.player.current_sprite]

    def update(self):
        self.player.check_collision()

        if self.player.velocity[0] == -1:
            self.player.image = pygame.transform.flip(self.player.image, True, False)
        elif self.player.velocity[0] == 1:
            self.player.image = pygame.transform.flip(self.player.image, False, False)


        if self.player.rect.colliderect(self.floor):
            self.player.velocity[1] = 0
            self.player.is_jumping = True
        else:
            self.player.velocity[1] += self.gravity

    def display(self):
        self.screen.blit(self.bg, (0, 0))
        self.player.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_event()
            self.update()
            self.display()
            self.clock.tick(120)
