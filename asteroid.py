import pygame

class Asteroid(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 100
        self.movey = 100
        self.image =pygame.image.load('asteroid.png')
        self.image =pygame.transform.smoothscale(self.image,(70,70))
        self.rect = self.image.get_rect()
        self.speed = pygame.math.Vector2(10,0)
        self.rect.x=x
        self.rect.y=y
    def move(self):
        self.rect.x += self.speed[0]