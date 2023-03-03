import pygame
import time
import scrambler
import times
import cube

from platform import system


def main():
    # Prefer globals than parameters for this since not returning from this funciton and it might be better for memory...not sure
    global time_text_colour, scramble, scramble_text, scramble_text_rect, time_text, time_text_rect, ao5s_text, ao5s_text_rect, ao12s_text, ao12s_text_rect, new_scramble_text, new_scramble_text_rect

    # Times list from json file
    read_times_list = times.get_times_list()
    if len(read_times_list.keys()) == 0:
        current_solve_time = "-"
        ao5 = "-"
        ao12 = "-"
    else:
        current_solve_time = read_times_list[str(len(read_times_list.keys()) - 1)]["time"]
        ao5 = read_times_list[str(len(read_times_list.keys()) - 1)]["ao5"]
        ao12 = read_times_list[str(len(read_times_list.keys()) - 1)]["ao12"]

    # Records from json file
    read_records = times.get_records()
    time_pb = read_records["time"]
    ao5_pb = read_records["ao5"]
    ao12_pb = read_records["ao12"]

    # Current solving state and time
    solving = False
    solve_time = 0

    # Used for exit confirmation window
    quitting = False

    while True:
        # Clean screen
        screen.fill(screen_bg_colour)

        # Check events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Escape key activates exit confirmation window
                if event.key == pygame.K_ESCAPE:
                    quitting = True

                if not quitting and event.key == pygame.K_SPACE:
                    # Turn green to indicate about to start timer
                    if not solving:
                        time_text_colour = (0,221,0)
                    else:
                        # Get new scramble
                        scramble = scrambler.get_scramble()

            if not quitting and event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                # Stop timer and update times
                if solving:
                    solving = False
                    current_time = time.time()
                    solve_time = current_time - start_time

                    times.add_times_list(read_times_list, scramble, round(solve_time, 2))

                    read_times_list = times.get_times_list()
                    current_solve_time = read_times_list[str(len(read_times_list.keys()) - 1)]["time"]
                    ao5 = read_times_list[str(len(read_times_list.keys()) - 1)]["ao5"]
                    ao12 = read_times_list[str(len(read_times_list.keys()) - 1)]["ao12"]

                    times.add_record(read_records, read_times_list)
                    
                    read_records = times.get_records()
                    time_pb = read_records["time"]
                    ao5_pb = read_records["ao5"]
                    ao12_pb = read_records["ao12"]
                else:
                    # Initiate timer
                    time_text_colour = "grey"
                    solving = True
                    start_time = time.time()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if quitting:
                    # Answer no to quit confirmation message
                    if exit_no_bg_rect.collidepoint(pygame.mouse.get_pos()):
                        quitting = False
                    # Answer yes to quit confirmation message and quit program
                    elif exit_yes_bg_rect.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        exit()
                else:
                    # get new scramble
                    if new_scramble_text_rect.collidepoint(pygame.mouse.get_pos()):
                        scramble = scrambler.get_scramble()

        # Mouse hover effects
        if ((not quitting and new_scramble_text_rect.collidepoint(pygame.mouse.get_pos())) or
            (quitting and exit_no_bg_rect.collidepoint(pygame.mouse.get_pos())) or
            (quitting and exit_yes_bg_rect.collidepoint(pygame.mouse.get_pos()))):
            # set the cursor to the hand cursor
            pygame.mouse.set_cursor(pygame.cursors.tri_left)
        else:
            # set the cursor to the default arrow cursor
            pygame.mouse.set_cursor(pygame.cursors.arrow)

        # Update solve time
        if solving:
            current_time = time.time()
            solve_time = current_time - start_time

        # Displays:
        # Scramble
        scramble_text, scramble_text_rect = scrambler.update_scramble(AnonymousPro_font,screen_width, screen, scramble, new_scramble_text, new_scramble_text_rect)

        # Logo
        screen.blit(twisttimer_logo, twisttimer_logo_rect)

        # Session
        screen.blit(current_session_text, current_session_text_rect)
        screen.blit(best_session_text, best_session_text_rect)

        screen.blit(time_session_text, time_session_text_rect)
        times.update_current_session_time(AnonymousPro_font_session, blue_time_text_colour, digit_char, screen, current_solve_time)
        times.update_record_session_time(AnonymousPro_font_session, blue_time_text_colour, digit_char, screen, time_pb, best_time_session_text_rect)

        screen.blit(ao5_session_text, ao5_session_text_rect)
        times.update_current_session_ao5(AnonymousPro_font_session, blue_time_text_colour, digit_char, screen, ao5)
        times.update_record_session_ao5(AnonymousPro_font_session, blue_time_text_colour, digit_char, screen, ao5_pb, best_ao5_session_text_rect)

        screen.blit(ao12_session_text, ao12_session_text_rect)
        times.update_current_session_ao12(AnonymousPro_font_session, blue_time_text_colour, digit_char, screen, ao12)
        times.update_record_session_ao12(AnonymousPro_font_session, blue_time_text_colour, digit_char, screen, ao12_pb, best_ao12_session_text_rect)

        pygame.draw.line(screen, "grey", (220, 150), (220, screen_height), width = 3)

        # Current times (time/ao5/ao12)
        time_text, time_text_rect = times.update_time(solve_time, time_text_colour, digit_char, digital_7_font, screen_width, screen_height, screen)
        ao5s_text, ao5s_text_rect = times.update_timer_ao5(AnonymousPro_font_aos, blue_time_text_colour, digit_char, screen_width, screen_height, screen, ao5)
        ao12s_text, ao12s_text_rect = times.update_timer_ao12(AnonymousPro_font_aos, blue_time_text_colour, digit_char, screen_width, screen_height, screen, ao12)

        # Cube scramble
        cube.draw_scramble(scramble, screen_width, screen_height, screen)

        # Exit confirmation
        if quitting:
            screen.fill("white", (screen_width/2 - 300, screen_height/2 - 150, 600, 350))
            pygame.draw.rect(screen, "black", (screen_width/2 - 300, screen_height/2 - 150, 600, 350), width = 5)

            screen.blit(exit_text, exit_text_rect)

            screen.blit(exit_text_question, exit_text_rect_question)

            screen.fill(blue_time_text_colour, exit_no_bg_rect)
            screen.blit(exit_text_no, exit_text_no_rect)
            pygame.draw.rect(screen, "black", exit_no_bg_rect, width = 3)

            screen.fill(blue_time_text_colour, exit_yes_bg_rect)
            screen.blit(exit_text_yes, exit_text_yes_rect)
            pygame.draw.rect(screen, "black", exit_yes_bg_rect, width = 3)

        pygame.display.update()


if __name__ != "__main__":
    # inits bruv
    pygame.init()

    # Digit character is different for formatting on different systems
    digit_char = "-"
    if system() == 'Windows':
        digit_char = "#"

    # Set window icon
    icon_surface = pygame.Surface((32, 32))
    icon_surface.fill('yellow', (0, 0, 10, 10))
    icon_surface.fill('yellow', (11, 0, 10, 10))
    icon_surface.fill('yellow', (22, 0, 10, 10))
    icon_surface.fill('red', (0, 11, 10, 10))
    icon_surface.fill('yellow', (11, 11, 10, 10))
    icon_surface.fill('green', (22, 11, 10, 10))
    icon_surface.fill('blue', (0, 22, 10, 10))
    icon_surface.fill('yellow', (11, 22, 10, 10))
    icon_surface.fill('white', (22, 22, 10, 10))
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

    # Scramble display
    AnonymousPro_font = pygame.font.Font("Fonts/AnonymousPro.ttf", 30)
    scramble = scrambler.get_scramble()

    blue_time_text_colour = (34,136,221)

    # New scramble display
    AnonymousPro_font_new_scramble = pygame.font.Font("Fonts/AnonymousPro.ttf", 20)
    new_scramble_text = AnonymousPro_font_new_scramble.render("next", True, blue_time_text_colour)
    new_scramble_text_rect = new_scramble_text.get_rect(topright = (screen_width - 160, 70))

    # ao5 and ao12 display
    AnonymousPro_font_aos = pygame.font.Font("Fonts/AnonymousPro.ttf", 60)

    # Exit pygame display
    AnonymousPro_font_exit = pygame.font.Font("Fonts/AnonymousPro.ttf", 40)
    exit_text = AnonymousPro_font_exit.render("Exit TwistTimer", True, "black")
    exit_text_rect = exit_text.get_rect(midtop = (screen_width/2 - 90, screen_height/2 - 110))

    AnonymousPro_font_exit_question = pygame.font.Font("Fonts/AnonymousPro.ttf", 30)
    exit_text_question = AnonymousPro_font_exit_question.render("Do you want to exit TwistTimer?", True, "black")
    exit_text_rect_question = exit_text_question.get_rect(midtop = (screen_width/2 - 7, screen_height/2))

    exit_no_bg_rect = pygame.Rect(screen_width/2 + 30, screen_height/2 + 110, 100, 60)
    exit_text_no = AnonymousPro_font_exit_question.render("No", True, "white")
    exit_text_no_rect = exit_text_no.get_rect(center = (screen_width/2 + 80, screen_height/2 + 140))

    exit_yes_bg_rect = pygame.Rect((screen_width/2 + 160, screen_height/2 + 110, 100, 60))
    exit_text_yes = AnonymousPro_font_exit_question.render("Yes", True, "white")
    exit_text_yes_rect = exit_text_yes.get_rect(center = (screen_width/2 + 210, screen_height/2 + 140))

    # TwistTimer Logo
    CubeBold_font = pygame.font.Font("Fonts/CubeBold.ttf", 120)
    twisttimer_logo = CubeBold_font.render("TT", True, (187,136,0))
    twisttimer_logo_rect = twisttimer_logo.get_rect(topleft = (40, 15))

    # Session stats
    AnonymousPro_font_session = pygame.font.Font("Fonts/Riverna Side.otf", 15)
    current_session_text = AnonymousPro_font_session.render("current", True, "white")
    current_session_text_rect = current_session_text.get_rect(topleft = (80, 200))

    best_session_text = AnonymousPro_font_session.render("best", True, "white")
    best_session_text_rect = best_session_text.get_rect(topleft = (160, 200))

    time_session_text = AnonymousPro_font_session.render("time", True, "white")
    time_session_text_rect = time_session_text.get_rect(topleft = (20, 240))

    current_time_session_text = AnonymousPro_font_session.render("-", True, blue_time_text_colour)
    current_time_session_text_rect = current_time_session_text.get_rect(midtop = (105, 240))

    best_time_session_text = AnonymousPro_font_session.render("-", True, blue_time_text_colour)
    best_time_session_text_rect = best_time_session_text.get_rect(midtop = (173, 240))

    ao5_session_text = AnonymousPro_font_session.render("ao5", True, "white")
    ao5_session_text_rect = ao5_session_text.get_rect(topleft = (20, 280))

    current_ao5_session_text = AnonymousPro_font_session.render("-", True, blue_time_text_colour)
    current_ao5_session_text_rect = current_ao5_session_text.get_rect(midtop = (105, 280))

    best_ao5_session_text = AnonymousPro_font_session.render("-", True, blue_time_text_colour)
    best_ao5_session_text_rect = best_ao5_session_text.get_rect(midtop = (173, 280))

    ao12_session_text = AnonymousPro_font_session.render("ao12", True, "white")
    ao12_session_text_rect = ao12_session_text.get_rect(topleft = (20, 320))

    current_ao12_session_text = AnonymousPro_font_session.render("-", True, blue_time_text_colour)
    current_ao12_session_text_rect = current_ao12_session_text.get_rect(midtop = (105, 320))

    best_ao12_session_text = AnonymousPro_font_session.render("-", True, blue_time_text_colour)
    best_ao12_session_text_rect = best_ao12_session_text.get_rect(midtop = (173, 320))

    main()

# TODO: add black border to yes/no buttons in exit confirmation screen
