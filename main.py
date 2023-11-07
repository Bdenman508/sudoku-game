import pygame

pygame.font.init()

font1 = pygame.font.SysFont("times", 40)
font2 = pygame.font.SysFont("times", 20)


def get_position(pos):
    global x
    x = pos[0] // des
    global y
    y = pos[1] // des


screen = pygame.display.set_mode((500, 600))


def game_msg():
    text1 = font2.render("Create your own Sudoku Board / Enter clues above", 1, (0, 0, 0))
    text2 = font2.render("Press C to clear board / D for default board", 1, (0, 0, 0))
    text3 = font2.render("Press Enter for AI to solve", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))
    screen.blit(text2, (20, 540))
    screen.blit(text3, (20, 560))


def end_game():
    text1 = font1.render("Great job AI", 1, (0, 0, 0))
    screen.blit(text1, (260, 555))


pygame.display.set_caption("Sudoku AI Solver")

x = 0
y = 0
des = 500 / 9
val = 0
# Create your own sudoku board
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def create_lines():
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                # color grid
                pygame.draw.rect(screen, (0, 255, 255), (i * des, j * des, des + 1, des + 1))

                # grid default numbers
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * des + 15, j * des + 15))
    # lines for grid
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * des), (500, i * des), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * des, 0), (i * des, 500), thick)


# entered cell value
def cell_value(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * des + 15, y * des + 15))


# make highlighted cell
def make_cell():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * des - 3, (y + i) * des), (x * des + des + 3, (y + i) * des), 7)
        pygame.draw.line(screen, (255, 0, 0), ((x + i) * des, y * des), ((x + i) * des, y * des + des), 7)

# Validity check
def check_valid(m, i, j, val):
    for it in range(9):
        if m[i][it] == val:
            return False
        if m[it][j] == val:
            return False
    it = i // 3
    jt = j // 3
    for i in range(it * 3, it * 3 + 3):
        for j in range(jt * 3, jt * 3 + 3):
            if m[i][j] == val:
                return False
    return True


# Backtracking Algorithm
def ai_solver(grid, i, j):
    while grid[i][j] != 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()
    for it in range(1, 10):
        if check_valid(grid, i, j, it) == True:
            grid[i][j] = it
            global x, y
            x = i
            y = j
            screen.fill((255, 255, 255))
            create_lines()
            make_cell()
            pygame.display.update()
            pygame.time.delay(20)
            if ai_solver(grid, i, j) == 1:
                return True
            else:
                grid[i][j] = 0
            screen.fill((255, 255, 255))
            create_lines()
            make_cell()
            pygame.display.update()
            pygame.time.delay(50)
    return False

run = True
box1 = 0
box2 = 0
rest = 0
err = 0

while run:

    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            box1 = 1
            pos = pygame.mouse.get_pos()
            get_position(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
                box1 = 1
            if event.key == pygame.K_RIGHT:
                x += 1
                box1 = 1
            if event.key == pygame.K_UP:
                y -= 1
                box1 = 1
            if event.key == pygame.K_DOWN:
                y += 1
                box1 = 1
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9
            if event.key == pygame.K_RETURN:
                box2 = 1
                # C to clear board
            if event.key == pygame.K_c:
                rest = 0
                box2 = 0
                grid = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            # D for default board
            if event.key == pygame.K_d:
                rest = 0
                box2 = 0
                grid = [
                    [4, 1, 0, 2, 7, 0, 8, 0, 5],
                    [0, 8, 5, 1, 4, 6, 0, 9, 7],
                    [0, 7, 0, 5, 8, 0, 0, 4, 0],
                    [9, 2, 7, 4, 5, 1, 3, 8, 6],
                    [5, 3, 8, 6, 9, 7, 4, 1, 2],
                    [1, 6, 4, 3, 2, 8, 7, 5, 9],
                    [8, 5, 2, 7, 0, 4, 9, 0, 0],
                    [0, 9, 0, 8, 0, 2, 5, 7, 4],
                    [7, 4, 0, 9, 6, 5, 0, 2, 8]
                ]
    if box2 == 1:
        if ai_solver(grid, 0, 0) == False:
            err = 1
        else:
            rest = 1
        box2 = 0
    if val != 0:
        cell_value(val)
        if check_valid(grid, int(x), int(y), val):
            grid[int(x)][int(y)] = val
            box1 = 0
        else:
            grid[int(x)][int(y)] = 0

        val = 0
    if rest == 1:
        end_game()
    create_lines()
    if box1 == 1:
        make_cell()
    game_msg()

    pygame.display.update()

pygame.quit()
