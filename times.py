import datetime


def update_time(solve_time, time_text_colour, digit_char, digital_7_font, screen_width, screen_height, screen):
    datetime_solve_time = datetime.datetime.fromtimestamp(solve_time)

    if int(solve_time) > 60:
        formatted_time = datetime_solve_time.strftime(f'%{digit_char}M:%S.%f')
    else:
        formatted_time = datetime_solve_time.strftime(f'%{digit_char}S.%f')

    time_text = digital_7_font.render(formatted_time[:-4], True, time_text_colour)
    time_text_rect = time_text.get_rect(center = (screen_width//2, screen_height//2))

    screen.blit(time_text, time_text_rect)

    return time_text, time_text_rect


def update_timer_ao5(AnonymousPro_font_aos, aos_text_colour, screen_width, screen_height, screen, ao5_time = "-"):
    ao5s_text = AnonymousPro_font_aos.render(f"ao5: {ao5_time}", True, aos_text_colour)
    ao5s_text_rect = ao5s_text.get_rect(midtop = (screen_width//2, screen_height//2 + 120))

    screen.blit(ao5s_text, ao5s_text_rect)

    return ao5s_text, ao5s_text_rect


def update_timer_ao12(AnonymousPro_font_aos, aos_text_colour, screen_width, screen_height, screen, ao12_time = "-"):
    ao12s_text = AnonymousPro_font_aos.render(f"ao12: {ao12_time}", True, aos_text_colour)
    ao12s_text_rect = ao12s_text.get_rect(midtop = (screen_width//2, screen_height//2 + 180))

    screen.blit(ao12s_text, ao12s_text_rect)

    return ao12s_text, ao12s_text_rect
