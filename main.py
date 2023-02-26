import pygame
import time


def main():
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                exit()
    # print("TwistTimer")

    # input("0.00")
    # start_time = time.time()

    # input("solve")
    # end_time = time.time()

    # time_passed = round(end_time - start_time, 2)
    # print(time_passed)
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
