import pygame

class Planet(pygame.sprite.Sprite):
    def __init__(self, x, y,pln,plna):
        screen_info = pygame.display.Info()
        size = (width, height) = ((int(screen_info.current_w), int(screen_info.current_h)))
        pygame.sprite.Sprite.__init__(self)
        self.movex = 100
        self.movey = 100
        self.image = pygame.image.load('planet.png')
        self.image = pygame.transform.smoothscale(self.image, (pln, plna))
        self.rect = self.image.get_rect()

        self.rect.x=x
        self.rect.y=y

    def update(self,enemyGroup):
        hitlist = pygame.sprite.spritecollide(self,enemyGroup, False)
        for enemy in hitlist:
            enemy.speed[0] *= -1
            enemy.speed[1] *= -1