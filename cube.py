import pygame


def move_side(cube_state, side, move):
    new_cube_state = cube_state.copy()

    if side == "F":
        while move:
            new_cube_state[6] = cube_state[17]
            new_cube_state[7] = cube_state[14]
            new_cube_state[8] = cube_state[11]
            new_cube_state[27] = cube_state[6]
            new_cube_state[30] = cube_state[7]
            new_cube_state[33] = cube_state[8]
            new_cube_state[47] = cube_state[27]
            new_cube_state[46] = cube_state[30]
            new_cube_state[45] = cube_state[33]
            new_cube_state[17] = cube_state[47]
            new_cube_state[14] = cube_state[46]
            new_cube_state[11] = cube_state[45]
            new_cube_state[18] = cube_state[24]
            new_cube_state[19] = cube_state[21]
            new_cube_state[20] = cube_state[18]
            new_cube_state[23] = cube_state[19]
            new_cube_state[26] = cube_state[20]
            new_cube_state[25] = cube_state[23]
            new_cube_state[24] = cube_state[26]
            new_cube_state[21] = cube_state[25]

            cube_state = new_cube_state
            new_cube_state = cube_state.copy()

            move -= 1
    elif side == "R":
        while move:
            new_cube_state[8] = cube_state[26]
            new_cube_state[5] = cube_state[23]
            new_cube_state[2] = cube_state[20]
            new_cube_state[36] = cube_state[8]
            new_cube_state[39] = cube_state[5]
            new_cube_state[42] = cube_state[2]
            new_cube_state[53] = cube_state[36]
            new_cube_state[50] = cube_state[39]
            new_cube_state[47] = cube_state[42]
            new_cube_state[26] = cube_state[53]
            new_cube_state[23] = cube_state[50]
            new_cube_state[20] = cube_state[47]
            new_cube_state[27] = cube_state[33]
            new_cube_state[28] = cube_state[30]
            new_cube_state[29] = cube_state[27]
            new_cube_state[32] = cube_state[28]
            new_cube_state[35] = cube_state[29]
            new_cube_state[34] = cube_state[32]
            new_cube_state[33] = cube_state[35]
            new_cube_state[30] = cube_state[34]

            cube_state = new_cube_state
            new_cube_state = cube_state.copy()

            move -= 1
    elif side == "U":
        while move:
            new_cube_state[38] = cube_state[11]
            new_cube_state[37] = cube_state[10]
            new_cube_state[36] = cube_state[9]
            new_cube_state[29] = cube_state[38]
            new_cube_state[28] = cube_state[37]
            new_cube_state[27] = cube_state[36]
            new_cube_state[20] = cube_state[29]
            new_cube_state[19] = cube_state[28]
            new_cube_state[18] = cube_state[27]
            new_cube_state[11] = cube_state[20]
            new_cube_state[10] = cube_state[19]
            new_cube_state[9] = cube_state[18]
            new_cube_state[0] = cube_state[6]
            new_cube_state[1] = cube_state[3]
            new_cube_state[2] = cube_state[0]
            new_cube_state[5] = cube_state[1]
            new_cube_state[8] = cube_state[2]
            new_cube_state[7] = cube_state[5]
            new_cube_state[6] = cube_state[8]
            new_cube_state[3] = cube_state[7]

            cube_state = new_cube_state
            new_cube_state = cube_state.copy()

            move -= 1
    elif side == "B":
        while move:
            new_cube_state[2] = cube_state[35]
            new_cube_state[1] = cube_state[32]
            new_cube_state[0] = cube_state[29]
            new_cube_state[9] = cube_state[2]
            new_cube_state[12] = cube_state[1]
            new_cube_state[15] = cube_state[0]
            new_cube_state[51] = cube_state[9]
            new_cube_state[52] = cube_state[12]
            new_cube_state[53] = cube_state[15]
            new_cube_state[35] = cube_state[51]
            new_cube_state[32] = cube_state[52]
            new_cube_state[29] = cube_state[53]
            new_cube_state[36] = cube_state[42]
            new_cube_state[37] = cube_state[39]
            new_cube_state[38] = cube_state[36]
            new_cube_state[41] = cube_state[37]
            new_cube_state[44] = cube_state[38]
            new_cube_state[43] = cube_state[41]
            new_cube_state[42] = cube_state[44]
            new_cube_state[39] = cube_state[43]

            cube_state = new_cube_state
            new_cube_state = cube_state.copy()

            move -= 1
    elif side == "L":
        while move:
            new_cube_state[0] = cube_state[44]
            new_cube_state[3] = cube_state[41]
            new_cube_state[6] = cube_state[38]
            new_cube_state[18] = cube_state[0]
            new_cube_state[21] = cube_state[3]
            new_cube_state[24] = cube_state[6]
            new_cube_state[45] = cube_state[18]
            new_cube_state[48] = cube_state[21]
            new_cube_state[51] = cube_state[24]
            new_cube_state[44] = cube_state[45]
            new_cube_state[41] = cube_state[48]
            new_cube_state[38] = cube_state[51]
            new_cube_state[9] = cube_state[15]
            new_cube_state[10] = cube_state[12]
            new_cube_state[11] = cube_state[9]
            new_cube_state[14] = cube_state[10]
            new_cube_state[17] = cube_state[11]
            new_cube_state[16] = cube_state[14]
            new_cube_state[15] = cube_state[17]
            new_cube_state[12] = cube_state[16]

            cube_state = new_cube_state
            new_cube_state = cube_state.copy()

            move -= 1
    else:
        while move:
            new_cube_state[24] = cube_state[15]
            new_cube_state[25] = cube_state[16]
            new_cube_state[26] = cube_state[17]
            new_cube_state[33] = cube_state[24]
            new_cube_state[34] = cube_state[25]
            new_cube_state[35] = cube_state[26]
            new_cube_state[42] = cube_state[33]
            new_cube_state[43] = cube_state[34]
            new_cube_state[44] = cube_state[35]
            new_cube_state[15] = cube_state[42]
            new_cube_state[16] = cube_state[43]
            new_cube_state[17] = cube_state[44]
            new_cube_state[45] = cube_state[51]
            new_cube_state[46] = cube_state[48]
            new_cube_state[47] = cube_state[45]
            new_cube_state[50] = cube_state[46]
            new_cube_state[53] = cube_state[47]
            new_cube_state[52] = cube_state[50]
            new_cube_state[51] = cube_state[53]
            new_cube_state[48] = cube_state[52]

            cube_state = new_cube_state
            new_cube_state = cube_state.copy()

            move -= 1

    return new_cube_state


def draw_scramble(scramble, screen_width, screen_height, screen):
    cube_state = [
        # Top
        "white", "white", "white",
        "white", "white", "white",
        "white", "white", "white",
        # Left
        "orange", "orange", "orange",
        "orange", "orange", "orange",
        "orange", "orange", "orange",
        # Front
        "green", "green", "green",
        "green", "green", "green",
        "green", "green", "green",
        # Right
        "red", "red", "red",
        "red", "red", "red",
        "red", "red", "red",
        # Back
        "blue", "blue", "blue",
        "blue", "blue", "blue",
        "blue", "blue", "blue",
        # Bottom
        "yellow", "yellow", "yellow",
        "yellow", "yellow", "yellow",
        "yellow", "yellow", "yellow"
    ]

    # Scramble cube state:
    new_cube_state = cube_state.copy()

    for scramble_move in scramble.split(" "):
        if len(scramble_move) == 1:
            new_cube_state = move_side(cube_state, scramble_move[0], 1)
        elif scramble_move[1] == "2":
            new_cube_state = move_side(cube_state, scramble_move[0], 2)
        else:
            new_cube_state = move_side(cube_state, scramble_move[0], 3)

        cube_state = new_cube_state

    display_left = screen_width - 250
    display_top = screen_height - 250

    screen.fill((0,51,68), (display_left, display_top, 250, 250))
    pygame.draw.rect(screen, "grey", (display_left, display_top, 253, 253), width = 3)

    # White
    screen.fill("black", (display_left + 78, display_top + 50, 50, 50))
    screen.fill(cube_state[0], (display_left + 78, display_top + 50, 16, 16))
    screen.fill(cube_state[1], (display_left + 95, display_top + 50, 16, 16))
    screen.fill(cube_state[2], (display_left + 112, display_top + 50, 16, 16))
    screen.fill(cube_state[3], (display_left + 78, display_top + 67, 16, 16))
    screen.fill(cube_state[4], (display_left + 95, display_top + 67, 16, 16))
    screen.fill(cube_state[5], (display_left + 112, display_top + 67, 16, 16))
    screen.fill(cube_state[6], (display_left + 78, display_top + 84, 16, 16))
    screen.fill(cube_state[7], (display_left + 95, display_top + 84, 16, 16))
    screen.fill(cube_state[8], (display_left + 112, display_top + 84, 16, 16))
    # Orange
    screen.fill("black", (display_left + 25, display_top + 103, 50, 50))
    screen.fill(cube_state[9], (display_left + 25, display_top + 103, 16, 16))
    screen.fill(cube_state[10], (display_left + 42, display_top + 103, 16, 16))
    screen.fill(cube_state[11], (display_left + 59, display_top + 103, 16, 16))
    screen.fill(cube_state[12], (display_left + 25, display_top + 120, 16, 16))
    screen.fill(cube_state[13], (display_left + 42, display_top + 120, 16, 16))
    screen.fill(cube_state[14], (display_left + 59, display_top + 120, 16, 16))
    screen.fill(cube_state[15], (display_left + 25, display_top + 137, 16, 16))
    screen.fill(cube_state[16], (display_left + 42, display_top + 137, 16, 16))
    screen.fill(cube_state[17], (display_left + 59, display_top + 137, 16, 16))
    # Green
    screen.fill("black", (display_left + 78, display_top + 103, 50, 50))
    screen.fill(cube_state[18], (display_left + 78, display_top + 103, 16, 16))
    screen.fill(cube_state[19], (display_left + 95, display_top + 103, 16, 16))
    screen.fill(cube_state[20], (display_left + 112, display_top + 103, 16, 16))
    screen.fill(cube_state[21], (display_left + 78, display_top + 120, 16, 16))
    screen.fill(cube_state[22], (display_left + 95, display_top + 120, 16, 16))
    screen.fill(cube_state[23], (display_left + 112, display_top + 120, 16, 16))
    screen.fill(cube_state[24], (display_left + 78, display_top + 137, 16, 16))
    screen.fill(cube_state[25], (display_left + 95, display_top + 137, 16, 16))
    screen.fill(cube_state[26], (display_left + 112, display_top + 137, 16, 16))
    # Red
    screen.fill("black", (display_left + 25 + 53*2, display_top + 50 + 53, 50, 50))
    screen.fill(cube_state[27], (display_left + 131, display_top + 103, 16, 16))
    screen.fill(cube_state[28], (display_left + 148, display_top + 103, 16, 16))
    screen.fill(cube_state[29], (display_left + 165, display_top + 103, 16, 16))
    screen.fill(cube_state[30], (display_left + 131, display_top + 120, 16, 16))
    screen.fill(cube_state[31], (display_left + 148, display_top + 120, 16, 16))
    screen.fill(cube_state[32], (display_left + 165, display_top + 120, 16, 16))
    screen.fill(cube_state[33], (display_left + 131, display_top + 137, 16, 16))
    screen.fill(cube_state[34], (display_left + 148, display_top + 137, 16, 16))
    screen.fill(cube_state[35], (display_left + 165, display_top + 137, 16, 16))
    # Blue
    screen.fill("black", (display_left + 25 + 53*3, display_top + 50 + 53, 50, 50))
    screen.fill(cube_state[36], (display_left + 184, display_top + 103, 16, 16))
    screen.fill(cube_state[37], (display_left + 201, display_top + 103, 16, 16))
    screen.fill(cube_state[38], (display_left + 218, display_top + 103, 16, 16))
    screen.fill(cube_state[39], (display_left + 184, display_top + 120, 16, 16))
    screen.fill(cube_state[40], (display_left + 201, display_top + 120, 16, 16))
    screen.fill(cube_state[41], (display_left + 218, display_top + 120, 16, 16))
    screen.fill(cube_state[42], (display_left + 184, display_top + 137, 16, 16))
    screen.fill(cube_state[43], (display_left + 201, display_top + 137, 16, 16))
    screen.fill(cube_state[44], (display_left + 218, display_top + 137, 16, 16))
    # Yell
    screen.fill("black", (display_left + 25 + 53, display_top + 50 + 53*2, 50, 50))
    screen.fill(cube_state[45], (display_left + 78, display_top + 156, 16, 16))
    screen.fill(cube_state[46], (display_left + 95, display_top + 156, 16, 16))
    screen.fill(cube_state[47], (display_left + 112, display_top + 156, 16, 16))
    screen.fill(cube_state[48], (display_left + 78, display_top + 173, 16, 16))
    screen.fill(cube_state[49], (display_left + 95, display_top + 173, 16, 16))
    screen.fill(cube_state[50], (display_left + 112, display_top + 173, 16, 16))
    screen.fill(cube_state[51], (display_left + 78, display_top + 190, 16, 16))
    screen.fill(cube_state[52], (display_left + 95, display_top + 190, 16, 16))
    screen.fill(cube_state[53], (display_left + 112, display_top + 190, 16, 16))
