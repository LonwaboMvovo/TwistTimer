def update_cube_type(AnonymousPro_font_cube_timer, screen_width, screen):
    cube_type_text = AnonymousPro_font_cube_timer.render("3x3x3", True, "white")
    cube_type_text_rect = cube_type_text.get_rect(center = (screen_width//2, 30))

    screen.blit(cube_type_text, cube_type_text_rect)

    return cube_type_text, cube_type_text_rect
