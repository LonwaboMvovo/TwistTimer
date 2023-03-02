import datetime
import json


def update_time(solve_time, time_text_colour, digit_char, digital_7_font, screen_width, screen_height, screen):
    datetime_solve_time = datetime.datetime.fromtimestamp(solve_time)

    # Format in min/sec/millisec
    if int(solve_time) > 59:
        formatted_time = datetime_solve_time.strftime(f'%{digit_char}M:%S.%f')
    # Format in sec/millisec
    else:
        formatted_time = datetime_solve_time.strftime(f'%{digit_char}S.%f')

    time_text = digital_7_font.render(formatted_time[:-4], True, time_text_colour)
    time_text_rect = time_text.get_rect(center = (screen_width//2, screen_height//2))

    screen.blit(time_text, time_text_rect)

    return time_text, time_text_rect


def update_timer_ao5(AnonymousPro_font_aos, aos_text_colour, digit_char, screen_width, screen_height, screen, ao5_time):
    # Average of 5 display
    if ao5_time == "-":
        ao5s_text = AnonymousPro_font_aos.render("ao5: -", True, aos_text_colour)
    else:
        # Format in min/sec/millisec
        datetime_ao5_time = datetime.datetime.fromtimestamp(ao5_time)

        if int(ao5_time) > 59:
            formatted_ao5_time = datetime_ao5_time.strftime(f'%{digit_char}M:%S.%f')[:-4]
        # Format in sec/millisec
        else:
            formatted_ao5_time = datetime_ao5_time.strftime(f'%{digit_char}S.%f')[:-4]

        ao5s_text = AnonymousPro_font_aos.render(f"ao5: {formatted_ao5_time}", True, aos_text_colour)

    ao5s_text_rect = ao5s_text.get_rect(midtop = (screen_width//2, screen_height//2 + 120))

    screen.blit(ao5s_text, ao5s_text_rect)

    return ao5s_text, ao5s_text_rect


def update_timer_ao12(AnonymousPro_font_aos, aos_text_colour, digit_char, screen_width, screen_height, screen, ao12_time):
    # Average of 12 display
    if ao12_time == "-":
        ao12s_text = AnonymousPro_font_aos.render("ao12: -", True, aos_text_colour)
    else:
        # Format in min/sec/millisec
        datetime_ao12_time = datetime.datetime.fromtimestamp(ao12_time)

        if int(ao12_time) > 59:
            formatted_ao12_time = datetime_ao12_time.strftime(f'%{digit_char}M:%S.%f')[:-4]
        # Format in sec/millisec
        else:
            formatted_ao12_time = datetime_ao12_time.strftime(f'%{digit_char}S.%f')[:-4]

        ao12s_text = AnonymousPro_font_aos.render(f"ao12: {formatted_ao12_time}", True, aos_text_colour)
    ao12s_text_rect = ao12s_text.get_rect(midtop = (screen_width//2, screen_height//2 + 180))

    screen.blit(ao12s_text, ao12s_text_rect)

    return ao12s_text, ao12s_text_rect


def update_current_session_time(AnonymousPro_font_session, blue_time_text_colour, digit_char, screen, current_solve_time):
    if current_solve_time != "-":
        # Format in min/sec/millisec
        datetime_current_solve_time = datetime.datetime.fromtimestamp(current_solve_time)

        if int(current_solve_time) > 59:
            current_solve_time_text = datetime_current_solve_time.strftime(f'%{digit_char}M:%S.%f')
        # Format in sec/millisec
        else:
            current_solve_time_text = datetime_current_solve_time.strftime(f'%{digit_char}S.%f')
    else:
        current_solve_time_text = "-"

    current_time_session_text = AnonymousPro_font_session.render(current_solve_time_text[:-4], True, blue_time_text_colour)
    current_time_session_text_rect = current_time_session_text.get_rect(midtop = (105, 240))
    screen.blit(current_time_session_text, current_time_session_text_rect)


def update_record_session_time(AnonymousPro_font_session, blue_time_text_colour, digit_char, screen, time_pb, best_time_session_text_rect):
    if time_pb != "-":
        # Format in min/sec/millisec
        datetime_time_pb = datetime.datetime.fromtimestamp(time_pb)

        if int(time_pb) > 59:
            time_pb_text = datetime_time_pb.strftime(f'%{digit_char}M:%S.%f')
        # Format in sec/millisec
        else:
            time_pb_text = datetime_time_pb.strftime(f'%{digit_char}S.%f')
    else:
        time_pb_text = "-"
    
    best_time_session_text = AnonymousPro_font_session.render(time_pb_text[:-4], True, blue_time_text_colour)
    best_time_session_text_rect = best_time_session_text.get_rect(midtop = (173, 240))
    screen.blit(best_time_session_text, best_time_session_text_rect)


def update_record_session_ao5(AnonymousPro_font_session, blue_time_text_colour, digit_char, screen, ao5_pb, best_ao5_session_text_rect):
    if ao5_pb != "-":
        # Format in min/sec/millisec
        datetime_ao5_pb = datetime.datetime.fromtimestamp(ao5_pb)

        if int(ao5_pb) > 59:
            ao5_pb_text = datetime_ao5_pb.strftime(f'%{digit_char}M:%S.%f')
        # Format in sec/millisec
        else:
            ao5_pb_text = datetime_ao5_pb.strftime(f'%{digit_char}S.%f')
    else:
        ao5_pb_text = "-"

    best_ao5_session_text = AnonymousPro_font_session.render(ao5_pb_text[:-4], True, blue_time_text_colour)
    best_ao5_session_text_rect = best_ao5_session_text.get_rect(midtop = (173, 280))
    screen.blit(best_ao5_session_text, best_ao5_session_text_rect)


def update_record_session_ao12(AnonymousPro_font_session, blue_time_text_colour, digit_char, screen, ao12_pb, best_ao12_session_text_rect):
    if ao12_pb != "-":
        # Format in min/sec/millisec
        datetime_ao12_pb = datetime.datetime.fromtimestamp(ao12_pb)

        if int(ao12_pb) > 59:
            ao12_pb_text = datetime_ao12_pb.strftime(f'%{digit_char}M:%S.%f')
        # Format in sec/millisec
        else:
            ao12_pb_text = datetime_ao12_pb.strftime(f'%{digit_char}S.%f')
    else:
        ao12_pb_text = "-"

    best_ao12_session_text = AnonymousPro_font_session.render(ao12_pb_text[:-4], True, blue_time_text_colour)
    best_ao12_session_text_rect = best_ao12_session_text.get_rect(midtop = (173, 320))
    screen.blit(best_ao12_session_text, best_ao12_session_text_rect)


def update_current_session_ao5(AnonymousPro_font_session, blue_time_text_colour, digit_char, screen, ao5):
    if ao5 != "-":
        # Format in min/sec/millisec
        datetime_ao5 = datetime.datetime.fromtimestamp(ao5)

        if int(ao5) > 59:
            ao5_text = datetime_ao5.strftime(f'%{digit_char}M:%S.%f')
        # Format in sec/millisec
        else:
            ao5_text = datetime_ao5.strftime(f'%{digit_char}S.%f')
    else:
        ao5_text = "-"

    current_ao5_session_text = AnonymousPro_font_session.render(ao5_text[:-4], True, blue_time_text_colour)
    current_ao5_session_text_rect = current_ao5_session_text.get_rect(midtop = (105, 280))
    screen.blit(current_ao5_session_text, current_ao5_session_text_rect)


def update_current_session_ao12(AnonymousPro_font_session, blue_time_text_colour, digit_char, screen, ao12):
    if ao12 != "-":
        # Format in min/sec/millisec
        datetime_ao12 = datetime.datetime.fromtimestamp(ao12)

        if int(ao12) > 59:
            ao12_text = datetime_ao12.strftime(f'%{digit_char}M:%S.%f')
        # Format in sec/millisec
        else:
            ao12_text = datetime_ao12.strftime(f'%{digit_char}S.%f')
    else:
        ao12_text = "-"

    current_ao12_session_text = AnonymousPro_font_session.render(ao12_text[:-4], True, blue_time_text_colour)
    current_ao12_session_text_rect = current_ao12_session_text.get_rect(midtop = (105, 320))
    screen.blit(current_ao12_session_text, current_ao12_session_text_rect)


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


def get_records():
    with open("Logs/records.json", "r") as file:
        read_records = json.load(file)

    return read_records


def add_record(records, times_list):
    last_time_info = times_list[str(len(times_list) -1)]
    last_time = last_time_info["time"]
    last_ao5 = last_time_info["ao5"]
    last_ao12 = last_time_info["ao12"]

    record_time = records["time"]
    record_ao5 = records["ao5"]
    record_ao12 = records["ao12"]

    if last_time != "-":
        if (record_time == "-") or (record_time != "-" and last_time < record_time):
            record_time = last_time

    if last_ao5 != "-":
        if (record_ao5 == "-") or (record_ao5 != "-" and last_ao5 < record_ao5):
            record_ao5 = last_ao5

    if last_ao12 != "-":
        if (record_ao12 == "-") or (record_ao12 != "-" and last_ao12 < record_ao12):
            record_ao12 = last_ao12

    records = {
        "time": record_time,
        "ao5": record_ao5,
        "ao12": record_ao12
    }

    records_json = json.dumps(records, indent=4)

    with open("Logs/records.json", "w") as outfile:
        outfile.write(records_json)
