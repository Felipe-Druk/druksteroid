import pygame   

from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(F"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    #Time
    clock = pygame.time.Clock()
    dt = 0

    #Screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill("black")

        clock.tick(60)
        dt = clock.get_time() / 1000.0 
        pygame.display.flip()


if __name__ == "__main__":
    main()
