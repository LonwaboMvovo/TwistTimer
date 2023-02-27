import pygame
import time
import json
import scrambler
import times

from platform import system


def update_cube_type():
    global cube_type_text, cube_type_text_rect

    cube_type_text = AnonymousPro_font_cube_timer.render("3x3x3", True, "white")
    cube_type_text_rect = cube_type_text.get_rect(center = (screen_width//2, 30))

    screen.blit(cube_type_text, cube_type_text_rect)


def main():
    global time_text_colour, scramble, scramble_text, scramble_text_rect, time_text, time_text_rect, ao5s_text, ao5s_text_rect, ao12s_text, ao12s_text_rect

    solving = False
    solve_time = 0

    while True:
        # Clean screen
        screen.fill(screen_bg_colour)

        # Check events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

                if event.key == pygame.K_SPACE:
                    if not solving:
                        time_text_colour = (0,221,0)
                    else:
                        scramble = scrambler.get_scramble()
            
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

        # Mouse hover effects
        if cube_type_text_rect.collidepoint(pygame.mouse.get_pos()):
            # set the cursor to the hand cursor
            pygame.mouse.set_cursor(pygame.cursors.tri_left)
        else:
            # set the cursor to the default arrow cursor
            pygame.mouse.set_cursor(pygame.cursors.arrow)

        if solving:
            current_time = time.time()
            solve_time = current_time - start_time

        update_cube_type()

        scramble_text, scramble_text_rect = scrambler.update_scramble(AnonymousPro_font,screen_width, screen, scramble)

        time_text, time_text_rect = times.update_time(solve_time, time_text_colour, digit_char, digital_7_font, screen_width, screen_height, screen)
        ao5s_text, ao5s_text_rect = times.update_timer_ao5(AnonymousPro_font_aos, aos_text_colour, screen_width, screen_height, screen)
        ao12s_text, ao12s_text_rect = times.update_timer_ao12(AnonymousPro_font_aos, aos_text_colour, screen_width, screen_height, screen)

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
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    screen_bg_colour = (0,34,51)
    screen.fill(screen_bg_colour)

    # Time display
    digital_7_font = pygame.font.Font("Fonts/digital-7.ttf", 250)
    time_text_colour = "grey"
    time_text = digital_7_font.render(f"{0:.2f}", True, time_text_colour)
    time_text_rect = time_text.get_rect(center = (screen_width//2, screen_height//2))

    # Scramble display
    AnonymousPro_font = pygame.font.Font("Fonts/AnonymousPro.ttf", 30)
    scramble = scrambler.get_scramble()
    scramble_text = AnonymousPro_font.render(scramble, True, "grey")
    scramble_text_rect = scramble_text.get_rect(center = (screen_width//2, 80))

    # Cube type display
    AnonymousPro_font_cube_timer = pygame.font.Font("Fonts/AnonymousPro.ttf", 20)
    cube_type_text = AnonymousPro_font_cube_timer.render("3x3x3", True, "white")
    cube_type_text_rect = cube_type_text.get_rect(center = (screen_width//2, 30))

    # ao5 and ao12 display
    AnonymousPro_font_aos = pygame.font.Font("Fonts/AnonymousPro.ttf", 60)
    aos_text_colour = (34,136,221)
    ao5s_text = AnonymousPro_font_aos.render("ao5: -", True, aos_text_colour)
    ao12s_text = AnonymousPro_font_aos.render("ao12: -", True, aos_text_colour)
    ao5s_text_rect = ao5s_text.get_rect(midtop = (screen_width//2, screen_height//2 + 120))
    ao12s_text_rect = ao12s_text.get_rect(midtop = (screen_width//2, screen_height//2 + 180))

    main()
