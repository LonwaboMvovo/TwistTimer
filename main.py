import pygame
import time


def time_solve():
    pass


def main():
    solving = False

    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if not solving:
                    solving = True
                    print("solving...")
                    start_time = time.time()
                else:
                    solving = False
                    print("finish...")
                    current_time = time.time()
                    time_passed = current_time - start_time
                    print(f'{time_passed:.2f}')

        if solving:
            current_time = time.time()
            time_passed = current_time - start_time
            print(f'{time_passed:.2f}')

        # Update screen/display
        pygame.display.update()
        # max set to 60 frames/sec
        clock.tick(60)


if __name__ == "__main__":
    # inits bruv
    pygame.init()
    clock = pygame.time.Clock()

    # Set window icon
    icon_surface = pygame.Surface((32, 32))
    icon_surface.fill('light green')
    # cube_icon = pygame.image.load('images/cube_icon.png')
    pygame.display.set_icon(icon_surface)

    # Set Window title
    pygame.display.set_caption("TwistTimer")

    # Set background
    screen = pygame.display.set_mode((1200, 700))
    screen_bg_colour = (0,34,51)
    screen.fill(screen_bg_colour)

    main()
