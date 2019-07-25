import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 100
        self.movey = 100
        self.image =pygame.image.load('ship.png')
        self.image =pygame.transform.smoothscale(self.image,(130,170))
        self.rect = self.image.get_rect()
        self.speed = pygame.math.Vector2(0,0)
        self.health =10


    def update(self,enemyGroup):
        self.rect.move_ip(self.speed)
        hitlist = pygame.sprite.spritecollide(self,enemyGroup, False)
        for enemy in hitlist:
            self.health -= 1
            print(self.health)