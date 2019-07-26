import sys,pygame
from ship import Ship
from asteroid import Asteroid
from planet import Planet
from health import Health

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
enemy = Asteroid(300,500,10,10,4,7)
enemy2 = Asteroid(1000,500,50,50,0,2,1)
enemy3 = Asteroid(140,200,40,40,5,7)
enemy4 = Asteroid(300,150,300,300,5,5)
enemy5 = Asteroid(30,400,70,70,3,3,)
enemy6 = Asteroid(0,600,50,50,7,5)
enemy7 = Asteroid(400,00,70,70,5,5)
enemy8 = Asteroid(30,100,30,30,4,7)
enemy9 = Asteroid(100,0,180,180,2,1)
enemy10 = Asteroid(50,800,200,0,5,7)
enemy11 = Asteroid(70,70,20,30,5,5)
enemy12 = Asteroid(1700,50,80,70,3,3,)
enemy13 = Asteroid(100,0,100,50,7,5)
enemy14 = Asteroid(590,400,70,70,5,5)
enemy15 = Asteroid(30,400,1000,1000,3,3,)
enemy16 = Asteroid(0,600,50,20,7,5)
enemy17 = Asteroid(400,400,760,700,5,5)
enemy18 = Asteroid(340,100,400,30,4,7)
enemy19 = Asteroid(100,0,500,180,2,1)
enemy20 = Asteroid(100,500,1000,500,5,7)



bumper = Planet(1000,100,50,50)
bumper2 = Planet(700,600,50,50)
bumper3 = Planet(600,0,50,50)
bumper4 = Planet(900,300,50,50)
bumper5 = Planet(400,600,50,50)


heart = Health(1000,0)

enemyGroup = pygame.sprite.Group()
enemyGroup.add(enemy2)
enemyGroup.add(enemy)
enemyGroup.add(enemy3)
enemyGroup.add(enemy4)
enemyGroup.add(enemy5)
enemyGroup.add(enemy6)
enemyGroup.add(enemy7)
enemyGroup.add(enemy8)
enemyGroup.add(enemy9)
enemyGroup.add(enemy10)
enemyGroup.add(enemy11)
enemyGroup.add(enemy12)
enemyGroup.add(enemy13)
enemyGroup.add(enemy14)



bumperGroup = pygame.sprite.Group()
bumperGroup.add(bumper)
bumperGroup.add(bumper2)
bumperGroup.add(bumper3)
bumperGroup.add(bumper4)
bumperGroup.add(bumper5)


heartGroup = pygame.sprite.Group()
heartGroup.add(heart)

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
                    Player.speed[0] = (-8)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right')
                    Player.speed[0] = (8)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    print('jump')
                    Player.speed[1] = (-8)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    print('down')
                    Player.speed[1] = (8)
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
        heart.update(Player.health)


        Player.update(enemyGroup,bumperGroup)
        for en in enemyGroup:
            en.move()
        for bumper in bumperGroup:
            bumper.update(enemyGroup)

        clock.tick(60)
        screen.fill(color)
        screen.blit(Player.image, Player.rect)
        bumperGroup.draw(screen)
        enemyGroup.draw(screen)
        heartGroup.draw(screen)
        pygame.display.flip()



if __name__ == '__main__':
    main()
