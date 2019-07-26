import pygame

class Asteroid(pygame.sprite.Sprite):




    def __init__(self,x,y,ast,asta,spd,spda):
        screen_info = pygame.display.Info()
        size = (width, height) = ((int(screen_info.current_w), int(screen_info.current_h)))

        pygame.sprite.Sprite.__init__(self)
        self.movex = 100
        self.movey = 100
        self.image =pygame.image.load('asteroid.png')
        self.image =pygame.transform.smoothscale(self.image,(ast,asta))
        self.rect = self.image.get_rect()
        self.speed = pygame.math.Vector2(spd,spda)
        self.rect.x=x
        self.rect.y=y
    def move(self):
        screen_info = pygame.display.Info()
        size = (width, height) = ((int(screen_info.current_w), int(screen_info.current_h)))

        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        if self.rect.bottom > height:
            self.speed[1] *= -1
        if self.rect.left < 0:
            self.speed[0] *= -1
        if self.rect.right > width:
            self.speed[0] *= -1
        if self.rect.top < 0:
            self.speed[1] *=- 1
