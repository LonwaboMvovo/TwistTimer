import re
import pygame

from random import choice as random_choice


def get_scramble():
    # All possible scramble moves
    scramble_moves = ["F", "R", "U", "B", "L", "D", "F2", "R2", "U2", "B2", "L2", "D2", "F'", "R'", "U'", "B'", "L'", "D'"]

    scramble = []

    # Add twenty random moves without back to back moves of the same side
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


def update_scramble(AnonymousPro_font,screen_width, screen, scramble, new_scramble_text, new_scramble_text_rect):
    # Scramble text display
    scramble_text = AnonymousPro_font.render(scramble, True, "grey")
    scramble_text_rect = scramble_text.get_rect(center = (screen_width//2, 80))

    screen.fill((0,51,68), (0, 0, screen_width, 150))
    pygame.draw.line(screen, "grey", (0, 150), (screen_width, 150), width = 3)

    screen.blit(scramble_text, scramble_text_rect)
    screen.blit(new_scramble_text, new_scramble_text_rect)

    return scramble_text, scramble_text_rect


if __name__ == "__main__":
    print(get_scramble())
