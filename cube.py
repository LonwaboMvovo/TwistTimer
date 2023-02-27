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

    screen.fill((0,51,68), (screen_width - 250, screen_height - 250, 250, 250))
    pygame.draw.rect(screen, "grey", (screen_width - 250, screen_height - 250, 253, 253), width = 3)
