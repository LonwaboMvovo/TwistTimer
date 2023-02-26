import pygame
import time


def main():
    solving = False

    solve_time = 0

    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if solving:
                    solving = False
                    current_time = time.time()
                    solve_time = current_time - start_time
                else:
                    solving = True
                    start_time = time.time()

        if solving:
            current_time = time.time()
            solve_time = current_time - start_time

        # Clean screen
        screen.fill(screen_bg_colour)

        # Update time
        time_text = pixel_type_font.render(f"{solve_time:.2f}", False, "grey")
        screen.blit(time_text, time_text_rect)

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
    icon_surface.fill('green')
    pygame.display.set_icon(icon_surface)

    # Set Window title
    pygame.display.set_caption("TwistTimer")

    # Set background
    screen = pygame.display.set_mode((1200, 700))
    screen_bg_colour = (0,34,51)
    screen.fill(screen_bg_colour)

    pixel_type_font = pygame.font.Font("font/digital-7.ttf", 300)
    time_text = pixel_type_font.render(f"{0:.2f}", True, "grey")
    time_text_rect = time_text.get_rect(center = (600, 350))
    main()
