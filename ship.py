import pygame


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        screen_info = pygame.display.Info()
        size = (width, height) = ((int(screen_info.current_w), int(screen_info.current_h)))
        pygame.sprite.Sprite.__init__(self)
        self.movex = 100
        self.movey = 100
        self.image =pygame.image.load('ship.png')
        self.image =pygame.transform.smoothscale(self.image,(130,170))
        self.rect = self.image.get_rect()
        self.speed = pygame.math.Vector2(0,0)
        self.health =10
        self.rect.center = (width//2, height//2)



    def update(self,enemyGroup):
        self.rect.move_ip(self.speed)
        hitlist = pygame.sprite.spritecollide(self,enemyGroup, False)
        for enemy in hitlist:
            self.health -= 1
            print(self.health)