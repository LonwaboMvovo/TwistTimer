import pygame
import time
import re

from random import choice as random_choice


def get_scramble():
    scramble_moves = ["F", "R", "U", "B", "L", "D", "F2", "R2", "U2", "B2", "L2", "D2", "F'", "R'", "U'", "B'", "L'", "D'"]

    scramble = []

    for _ in range(20):
        if len(scramble) == 0:
            scramble.append(random_choice(scramble_moves))
        else:
            last_scramble = scramble[-1]
            last_scramble_type = ''.join(w for w in re.split("["+"\\".join("2'")+"]", last_scramble))

            new_scramble = random_choice(scramble_moves)
            new_scramble_type = ''.join(w for w in re.split("["+"\\".join("2'")+"]", new_scramble))

            while last_scramble_type == new_scramble_type:
                new_scramble = random_choice(scramble_moves)
                new_scramble_type = ''.join(w for w in re.split("["+"\\".join("2'")+"]", new_scramble))

            scramble.append(new_scramble)
    
    return " ".join(scramble)


def update_time(solve_time, time_text_colour):
    time_text = pixel_type_font.render(f"{solve_time:.2f}", True, time_text_colour)
    screen.blit(time_text, time_text_rect)


def main():
    global time_text_colour

    solving = False
    solve_time = 0

    while True:
        # Check events
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not solving:
                    time_text_colour = (0,221,0)
            
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_SPACE:
                    if solving:
                        solving = False
                        current_time = time.time()
                        solve_time = current_time - start_time
                    else:
                        time_text_colour = "grey"
                        solving = True
                        start_time = time.time()

        if solving:
            current_time = time.time()
            solve_time = current_time - start_time

        # Clean screen
        screen.fill(screen_bg_colour)

        update_time(solve_time, time_text_colour)

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

    # Time display
    pixel_type_font = pygame.font.Font("font/digital-7.ttf", 300)
    time_text_colour = "grey"
    time_text = pixel_type_font.render(f"{0:.2f}", True, time_text_colour)
    time_text_rect = time_text.get_rect(center = (600, 350))

    main()
