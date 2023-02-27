import pygame

def update_cube_type(AnonymousPro_font_cube_timer, screen_width, screen):
    cube_type_text = AnonymousPro_font_cube_timer.render("3x3x3", True, "white")
    cube_type_text_rect = cube_type_text.get_rect(center = (screen_width//2, 30))

    screen.blit(cube_type_text, cube_type_text_rect)

    return cube_type_text, cube_type_text_rect


def draw_scramble(scramble, screen_width, screen_height, screen):
    cube_state = [
        # Top
        [["w", "w", "w"],
            ["w", "w", "w"],
            ["w", "w", "w"]
        ],
        # Left
        [["o", "o", "o"],
            ["o", "o", "o"],
            ["o", "o", "o"]
        ],
        # Front
        [["g", "g", "g"],
            ["g", "g", "g"],
            ["g", "g", "g"]
        ],
        # Right
        [["r", "r", "r"],
            ["r", "r", "r"],
            ["r", "r", "r"]
        ],
        # Back
        [["b", "b", "b"],
            ["b", "b", "b"],
            ["b", "b", "b"]
        ],
        # Bottom
        [["y", "y", "y"],
            ["y", "y", "y"],
            ["y", "y", "y"]
        ],
    ]

    display_left = screen_width - 250
    display_top = screen_height - 250

    screen.fill((0,51,68), (display_left, display_top, 250, 250))
    pygame.draw.rect(screen, "grey", (display_left, display_top, 253, 253), width = 3)

    # White
    screen.fill("black", (display_left + 78, display_top + 50, 50, 50))
    screen.fill("white", (display_left + 78, display_top + 50, 16, 16))
    screen.fill("white", (display_left + 95, display_top + 50, 16, 16))
    screen.fill("white", (display_left + 112, display_top + 50, 16, 16))
    screen.fill("white", (display_left + 78, display_top + 67, 16, 16))
    screen.fill("white", (display_left + 95, display_top + 67, 16, 16))
    screen.fill("white", (display_left + 112, display_top + 67, 16, 16))
    screen.fill("white", (display_left + 78, display_top + 84, 16, 16))
    screen.fill("white", (display_left + 95, display_top + 84, 16, 16))
    screen.fill("white", (display_left + 112, display_top + 84, 16, 16))
    # Orange
    screen.fill("black", (display_left + 25, display_top + 103, 50, 50))
    screen.fill("orange", (display_left + 25, display_top + 103, 16, 16))
    screen.fill("orange", (display_left + 42, display_top + 103, 16, 16))
    screen.fill("orange", (display_left + 59, display_top + 103, 16, 16))
    screen.fill("orange", (display_left + 25, display_top + 120, 16, 16))
    screen.fill("orange", (display_left + 42, display_top + 120, 16, 16))
    screen.fill("orange", (display_left + 59, display_top + 120, 16, 16))
    screen.fill("orange", (display_left + 25, display_top + 137, 16, 16))
    screen.fill("orange", (display_left + 42, display_top + 137, 16, 16))
    screen.fill("orange", (display_left + 59, display_top + 137, 16, 16))
    # Green
    screen.fill("black", (display_left + 78, display_top + 103, 50, 50))
    screen.fill("green", (display_left + 78, display_top + 103, 16, 16))
    screen.fill("green", (display_left + 95, display_top + 103, 16, 16))
    screen.fill("green", (display_left + 112, display_top + 103, 16, 16))
    screen.fill("green", (display_left + 78, display_top + 120, 16, 16))
    screen.fill("green", (display_left + 95, display_top + 120, 16, 16))
    screen.fill("green", (display_left + 112, display_top + 120, 16, 16))
    screen.fill("green", (display_left + 78, display_top + 137, 16, 16))
    screen.fill("green", (display_left + 95, display_top + 137, 16, 16))
    screen.fill("green", (display_left + 112, display_top + 137, 16, 16))
    # Red
    screen.fill("red", (display_left + 25 + 53*2, display_top + 50 + 53, 50, 50))
    screen.fill("black", (display_left + 25 + 53*2, display_top + 50 + 53, 50, 50))
    # Blue
    screen.fill("blue", (display_left + 25 + 53*3, display_top + 50 + 53, 50, 50))
    screen.fill("black", (display_left + 25 + 53*3, display_top + 50 + 53, 50, 50))
    # Yell
    screen.fill("yellow", (display_left + 25 + 53, display_top + 50 + 53*2, 50, 50))
    screen.fill("black", (display_left + 25 + 53, display_top + 50 + 53*2, 50, 50))
