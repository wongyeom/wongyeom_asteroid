import sys,pygame
from ship import Ship
from asteroid import Asteroid
pygame.init()

# from pygame. locals import *
pygame.init()
screen_info = pygame.display.Info()
# set the width and height to the size of screen
Player = Ship()
size = (width, height) = ((int(screen_info.current_w), int(screen_info.current_h)))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 0, 0)
enemy = Asteroid(10,10)
enemy2 = Asteroid(10000,10000)
enemy3 = Asteroid(700,200)
enemy4 = Asteroid(50,50)
enemy5 = Asteroid(30,400)
enemy6 = Asteroid(0,600)
enemy7 = Asteroid(400,400)




enemyGroup = pygame.sprite.Group()
enemyGroup.add(enemy2)
enemyGroup.add(enemy)
enemyGroup.add(enemy3)
enemyGroup.add(enemy4)
enemyGroup.add(enemy5)
enemyGroup.add(enemy6)
enemyGroup.add(enemy7)






def moveship():
    global Player
    global speed
    if Player.rect.top < (0):
        Player.speed[1] *= -1
    if Player.rect.right > width:
        Player.speed[0] *= -1

    if Player.rect.left < (0):
        Player.speed[0] *= -1

    if Player.rect.bottom > height:
        Player.speed[1] *= -1

def main():
    while True:
        global speed
        moveship()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print('left')
                    Player.speed[0] = (-2)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right')
                    Player.speed[0] = (2)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    print('jump')
                    Player.speed[1] = (-2)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    print('down')
                    Player.speed[1] = (2)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print('left stop')
                    Player.speed[0] = (0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right stop')
                    Player.speed[0] = (0)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    print('up stop')
                    Player.speed[1] = (0)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    print('down stop')
                    Player.speed[1] = (0)

        Player.update(enemyGroup)
        for en in enemyGroup:
            en.move()
        clock.tick(60)
        screen.fill(color)
        screen.blit(Player.image, Player.rect)
        enemyGroup.draw(screen)
        pygame.display.flip()



if __name__ == '__main__':
    main()
