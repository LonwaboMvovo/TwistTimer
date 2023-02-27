import datetime
import json


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


def get_times_list():
    with open("times_list.json", "r") as file:
        read_times_list = json.load(file)

    return read_times_list


def update_times_list(times_list, scramble, time, state = "OK"):
    date = "DD/MM/YYYY" # date of solve
    ao5 = 0.0 # ao5 of current solve time
    ao12 = 0.0 # ao12 of current solve time

    times_list[str(len(times_list.keys()))] = {
            "date": date,
            "scramble": scramble,
            "state": state,
            "time": time,
            "ao5": ao5,
            "ao12": ao12,
            "comment": "", # initially should be empty sting, then user can update if they want to add coment
        }

    times_list_json = json.dumps(times_list, indent=4)

    with open("times_list.json", "w") as outfile:
        outfile.write(times_list_json)


if __name__ == "__main__":
    update_times_list(get_times_list(), "D' R D' F L' B' L U B2 L' D2 L2 B2 U2 D2 U2 R D' L R2", 11.56)
