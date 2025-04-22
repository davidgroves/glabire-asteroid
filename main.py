import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Asteroids")

    # Initialize groups and set containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # Create the Player AFTER containers are set
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60) / 1000.0
        
        pygame.Surface.fill(screen, "black")
        for entity in drawable:
            entity.draw(screen)
        updatable.update(dt)
        pygame.display.flip()
  

if __name__ == "__main__":
    main()

