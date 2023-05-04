# Импортирую библиотеки

import pygame
from random import randrange


# Задаю переменные количества кадров ширины и высоты
Width = 800
Height = 600
FPS = 10

# Цвета
BLACK = (0, 0, 0)

# Переменные относящиеся к змейке
Zm_block = 20
Zm_list = []
lenght = 1
z_x = randrange(0, Width, Zm_block)
z_y = randrange(0, Height, Zm_block)
dx, dy = 0, 0
snake = [(z_x, z_y)]
apple = randrange(Zm_block, Width - Zm_block, Zm_block), randrange(Zm_block, Height - Zm_block, Zm_block)
Big_apple = randrange(Zm_block, Width - Zm_block, Zm_block), randrange(Zm_block, Height - Zm_block, Zm_block)
r = 25
dirs = {"W": True, "A": True, "S": True, "D": True}

# Создаём игру и окно
pygame.init()
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

# Счёт
score_font = pygame.font.SysFont("Arial", 20, bold=True)
end_font = pygame.font.SysFont("Arial", 40, bold=True)
score = 0

matrix = [[ "" for j in range(30)] for i in range(40)]

def lev(p, matrix):
    with open(p) as f:
         a = f.readlines()
         for i in range(len(a)):
              for j in range(30):
                   matrix[i][j] = a[i][j]

    return matrix                

game_run = True
while game_run:
    screen.fill(BLACK)

    [(pygame.draw.rect(screen, pygame.Color("white"), (i, j, Zm_block, Zm_block))) for i, j in snake]
    
    pygame.draw.rect(screen, pygame.Color("red"), (*apple, Zm_block, Zm_block))

    if r > 0:
        pygame.draw.circle(screen, pygame.Color("blue"), ( Big_apple[0] + 10, Big_apple[1] + 10 ), 8)
        r -= 1
    else:
        r = 25
        Big_apple = randrange(Zm_block, Width - Zm_block, Zm_block), randrange(Zm_block, Height - Zm_block, Zm_block)
        for i in range(len(snake)):
            while (Big_apple[0], Big_apple[1]) == snake[i]:
                        Big_apple = randrange(Zm_block, Width - Zm_block, Zm_block), randrange(Zm_block, Height - Zm_block, Zm_block)

    # Рендер надписи
    render_score = score_font.render(f'SCORE: {score}', 1, pygame.Color("white"))
    screen.blit(render_score, (5, 5))

    z_x += dx * Zm_block
    z_y += dy * Zm_block
    snake.append((z_x, z_y))
    snake = snake[-lenght:]

    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()

    # Держим цикл на правильной скорости
    clock.tick(FPS)

    # 
    if snake[-1] == apple:
        apple_x = randrange(Zm_block, Width - Zm_block, Zm_block)
        apple_y = randrange(Zm_block, Height - Zm_block, Zm_block)

        for i in range(len(snake)):
            while (apple_x, apple_y) == snake[i]:
                        apple_x = randrange(Zm_block, Width - Zm_block, Zm_block)
                        apple_y = randrange(Zm_block, Height - Zm_block, Zm_block)
        apple = apple_x, apple_y
        lenght += 1
        score += 10
        FPS += 1

    if snake[-1] == Big_apple:
        Big_apple = randrange(Zm_block, Width - Zm_block, Zm_block), randrange(Zm_block, Height - Zm_block, Zm_block)

        for i in range(len(snake)):
            while (Big_apple[0], Big_apple[1]) == snake[i]:
                        Big_apple = randrange(Zm_block, Width - Zm_block, Zm_block), randrange(Zm_block, Height - Zm_block, Zm_block)
        lenght += 1
        score += r
        FPS += 1
        r = 0
    
    if z_x < 0 or z_x > Width - Zm_block or z_y < 0 or z_y > Height - Zm_block or len(snake) != len(set(snake)):
        while True:
            render_end = end_font.render(f'Игра закончена. Ваш счёт:{score}', 1, pygame.Color("orange"))
            screen.blit(render_end, (100, Height/2))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
    
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs["W"]:
        dx, dy = 0, -1
        dirs = {"W": True, "A": True, "S": False, "D": True}

    if key[pygame.K_a] and dirs["A"]:
        dx, dy = -1, 0
        dirs = {"W": True, "A": True, "S": True, "D": False}

    if key[pygame.K_s] and dirs["S"]:
        dx, dy = 0, 1
        dirs = {"W": False, "A": True, "S": True, "D": True}

    if key[pygame.K_d] and dirs["D"]:
        dx, dy = 1, 0
        dirs = {"W": True, "A": False, "S": True, "D": True}

pygame.quit()
# Импортирую библиотеки

import pygame
from random import randrange


# Задаю переменные количества кадров ширины и высоты
Width = 800
Height = 600
FPS = 10

# Цвета
BLACK = (0, 0, 0)

# Переменные относящиеся к змейке
Zm_block = 20
Zm_list = []
lenght = 1
z_x = randrange(0, Width, Zm_block)
z_y = randrange(0, Height, Zm_block)
dx, dy = 0, 0
snake = [(z_x, z_y)]
apple = randrange(Zm_block, Width - Zm_block, Zm_block), randrange(Zm_block, Height - Zm_block, Zm_block)
Big_apple = randrange(Zm_block, Width - Zm_block, Zm_block), randrange(Zm_block, Height - Zm_block, Zm_block)
r = 25
dirs = {"W": True, "A": True, "S": True, "D": True}

# Создаём игру и окно
pygame.init()
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

# Счёт
score_font = pygame.font.SysFont("Arial", 20, bold=True)
end_font = pygame.font.SysFont("Arial", 40, bold=True)
score = 0

matrix = [[ "" for j in range(30)] for i in range(40)]

def lev(p, matrix):
    with open(p) as f:
         a = f.readlines()
         for i in range(len(a)):
              for j in range(30):
                   matrix[i][j] = a[i][j]

    return matrix                

game_run = True
while game_run:
    screen.fill(BLACK)

    [(pygame.draw.rect(screen, pygame.Color("white"), (i, j, Zm_block, Zm_block))) for i, j in snake]
    
    pygame.draw.rect(screen, pygame.Color("red"), (*apple, Zm_block, Zm_block))

    if r > 0:
        pygame.draw.circle(screen, pygame.Color("blue"), ( Big_apple[0] + 10, Big_apple[1] + 10 ), 8)
        r -= 1
    else:
        r = 25
        Big_apple = randrange(Zm_block, Width - Zm_block, Zm_block), randrange(Zm_block, Height - Zm_block, Zm_block)
        for i in range(len(snake)):
            while (Big_apple[0], Big_apple[1]) == snake[i]:
                        Big_apple = randrange(Zm_block, Width - Zm_block, Zm_block), randrange(Zm_block, Height - Zm_block, Zm_block)

    # Рендер надписи
    render_score = score_font.render(f'SCORE: {score}', 1, pygame.Color("white"))
    screen.blit(render_score, (5, 5))

    z_x += dx * Zm_block
    z_y += dy * Zm_block
    snake.append((z_x, z_y))
    snake = snake[-lenght:]

    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()

    # Держим цикл на правильной скорости
    clock.tick(FPS)

    # 
    if snake[-1] == apple:
        apple_x = randrange(Zm_block, Width - Zm_block, Zm_block)
        apple_y = randrange(Zm_block, Height - Zm_block, Zm_block)

        for i in range(len(snake)):
            while (apple_x, apple_y) == snake[i]:
                        apple_x = randrange(Zm_block, Width - Zm_block, Zm_block)
                        apple_y = randrange(Zm_block, Height - Zm_block, Zm_block)
        apple = apple_x, apple_y
        lenght += 1
        score += 10
        FPS += 1

    if snake[-1] == Big_apple:
        Big_apple = randrange(Zm_block, Width - Zm_block, Zm_block), randrange(Zm_block, Height - Zm_block, Zm_block)

        for i in range(len(snake)):
            while (Big_apple[0], Big_apple[1]) == snake[i]:
                        Big_apple = randrange(Zm_block, Width - Zm_block, Zm_block), randrange(Zm_block, Height - Zm_block, Zm_block)
        lenght += 1
        score += r
        FPS += 1
        r = 0
    
    if z_x < 0 or z_x > Width - Zm_block or z_y < 0 or z_y > Height - Zm_block or len(snake) != len(set(snake)):
        while True:
            render_end = end_font.render(f'Игра закончена. Ваш счёт:{score}', 1, pygame.Color("orange"))
            screen.blit(render_end, (100, Height/2))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
    
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs["W"]:
        dx, dy = 0, -1
        dirs = {"W": True, "A": True, "S": False, "D": True}

    if key[pygame.K_a] and dirs["A"]:
        dx, dy = -1, 0
        dirs = {"W": True, "A": True, "S": True, "D": False}

    if key[pygame.K_s] and dirs["S"]:
        dx, dy = 0, 1
        dirs = {"W": False, "A": True, "S": True, "D": True}

    if key[pygame.K_d] and dirs["D"]:
        dx, dy = 1, 0
        dirs = {"W": True, "A": False, "S": True, "D": True}

pygame.quit()
