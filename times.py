import datetime
import json


def update_time(solve_time, time_text_colour, digit_char, digital_7_font, screen_width, screen_height, screen):
    datetime_solve_time = datetime.datetime.fromtimestamp(solve_time)

    # Format in min/sec/millisec
    if int(solve_time) > 60:
        formatted_time = datetime_solve_time.strftime(f'%{digit_char}M:%S.%f')
    # Format in sec/millisec
    else:
        formatted_time = datetime_solve_time.strftime(f'%{digit_char}S.%f')

    time_text = digital_7_font.render(formatted_time[:-4], True, time_text_colour)
    time_text_rect = time_text.get_rect(center = (screen_width//2, screen_height//2))

    screen.blit(time_text, time_text_rect)

    return time_text, time_text_rect


def update_timer_ao5(AnonymousPro_font_aos, aos_text_colour, screen_width, screen_height, screen, ao5_time):
    # Average of 5 display
    if ao5_time == "-":
        ao5s_text = AnonymousPro_font_aos.render("ao5: -", True, aos_text_colour)
    else:
        ao5s_text = AnonymousPro_font_aos.render(f"ao5: {ao5_time:.2f}", True, aos_text_colour)
    ao5s_text_rect = ao5s_text.get_rect(midtop = (screen_width//2, screen_height//2 + 120))

    screen.blit(ao5s_text, ao5s_text_rect)

    return ao5s_text, ao5s_text_rect


def update_timer_ao12(AnonymousPro_font_aos, aos_text_colour, screen_width, screen_height, screen, ao12_time):
    # Average of 12 display
    if ao12_time == "-":
        ao12s_text = AnonymousPro_font_aos.render("ao12: -", True, aos_text_colour)
    else:
        ao12s_text = AnonymousPro_font_aos.render(f"ao12: {ao12_time:.2f}", True, aos_text_colour)
    ao12s_text_rect = ao12s_text.get_rect(midtop = (screen_width//2, screen_height//2 + 180))

    screen.blit(ao12s_text, ao12s_text_rect)

    return ao12s_text, ao12s_text_rect


def get_times_list():
    with open("Logs/times_list.json", "r") as file:
        read_times_list = json.load(file)

    return read_times_list


def add_times_list(times_list, scramble, time, state = "OK"):
    # Add solve to times_list json file
    current_date = datetime.date.today()
    formatted_date = current_date.strftime('%d/%m/%Y')

    ao5 = "-"
    if len(times_list.keys()) > 4:
        last_5_times = [times_list[t]["time"] for t in list(times_list.keys())[-5:]]
        ao5 = round(sum(last_5_times)/5, 2) # ao5 of current solve time

    ao12 = "-"
    if len(times_list.keys()) > 11:
        last_12_times = [times_list[t]["time"] for t in list(times_list.keys())[-12:]]
        ao12 = round(sum(last_12_times)/12, 2) # ao12 of current solve time

    times_list[len(times_list.keys())] = {
            "date": formatted_date,
            "scramble": scramble,
            "state": state,
            "time": time,
            "ao5": ao5,
            "ao12": ao12,
        }

    times_list_json = json.dumps(times_list, indent=4)

    with open("Logs/times_list.json", "w") as outfile:
        outfile.write(times_list_json)
