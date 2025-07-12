import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from bullet import *
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateables, drawables)
    AsteroidField.containers = (updateables)
    Player.containers = (updateables, drawables)
    Shot.containers = (shots, updateables, drawables)
    
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    af = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateables.update(dt)

        # Asteroid/player collision check
        for a in asteroids:
            if a.collide(p):
                print("Game over!")
                sys.exit()

        # Asteroid/Bullet collsion check
        for s in shots:
            for a in asteroids:
                if s.collide(a):
                    s.kill()
                    a.split()

        screen.fill("black")
        
        for obj in drawables:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
