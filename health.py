import pygame


class Health(pygame.sprite.Sprite):
    def __init__(self, x, y):
        screen_info = pygame.display.Info()
        size = (width, height) = ((int(screen_info.current_w), int(screen_info.current_h)))
        pygame.sprite.Sprite.__init__(self)
        self.movex = 100
        self.movey = 100
        self.image = pygame.image.load('health.png')
        self.image = pygame.transform.smoothscale(self.image, (50,50))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def update(self, health):
        if health <= 3:
            self.image = pygame.image.load('half.png')
            self.image = pygame.transform.smoothscale(self.image, (50,50))