import pygame
import time
import re
import datetime

from platform import system
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

def update_scramble(scramble):
    global scramble_text, scramble_text_rect

    scramble_text = AnonymousPro_font.render(scramble, True, scramble_text_colour)
    scramble_text_rect = scramble_text.get_rect(center = (600, 80))

    screen.blit(scramble_text, scramble_text_rect)


def update_time(solve_time, time_text_colour):
    global time_text, time_text_rect

    datetime_solve_time = datetime.datetime.fromtimestamp(solve_time)

    if int(solve_time) > 60:
        formatted_time = datetime_solve_time.strftime(f'%{digit_char}M:%S.%f')
    else:
        formatted_time = datetime_solve_time.strftime(f'%{digit_char}S.%f')

    time_text = digital_7_font.render(formatted_time[:-4], True, time_text_colour)
    time_text_rect = time_text.get_rect(center = (650, 350))

    screen.blit(time_text, time_text_rect)


def main():
    global time_text_colour, scramble

    solving = False
    solve_time = 0

    while True:
        # Clean screen
        screen.fill(screen_bg_colour)

        # Check events
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not solving:
                        time_text_colour = (0,221,0)
                    else:
                        scramble = get_scramble()
            
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

        update_scramble(scramble)
        update_time(solve_time, time_text_colour)

        pygame.display.update()


if __name__ == "__main__":
    # inits bruv
    pygame.init()

    # Digit character is different for formatting on different systems
    digit_char = "-"
    if system() == 'Windows':
        digit_char = "#"

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
    digital_7_font = pygame.font.Font("fonts/digital-7.ttf", 250)
    time_text_colour = "grey"
    time_text = digital_7_font.render(f"{0:.2f}", True, time_text_colour)
    time_text_rect = time_text.get_rect(center = (600, 350))

    # Scramble display
    AnonymousPro_font = pygame.font.Font("fonts/AnonymousPro.ttf", 30)
    scramble_text_colour = "grey"
    scramble = get_scramble()
    scramble_text = AnonymousPro_font.render(scramble, True, scramble_text_colour)
    scramble_text_rect = scramble_text.get_rect(center = (600, 80))

    main()
