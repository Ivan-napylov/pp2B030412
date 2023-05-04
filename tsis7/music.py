import pygame


pygame.init()
pygame.display.set_caption("Game")

screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()

o = []
o.append('music/bullet.mp3')
o.append('music/la_espada.mp3')
o.append('music/nikitata.mp3')
i = 0

pygame.mixer.music.load(o[i])
pygame.mixer.music.play()

running = True
while running:

    for p in pygame.event.get():
        if p.type == pygame.QUIT:
            running = False

        if p.type == pygame.KEYUP:

            if p.key == pygame.K_1:
                pygame.mixer.music.pause()

            elif p.key == pygame.K_2:
                pygame.mixer.music.play()

            elif p.key == pygame.K_3:
                pygame.mixer.music.pause()
                if (i != 2):
                    i += 1
                else:
                    i = 0
                pygame.mixer.music.load(o[i])
                pygame.mixer.music.play()

            elif p.key == pygame.K_4:
                pygame.mixer.music.pause()
                if (i != 0):
                    i -= 1
                else:
                    i = 2
                pygame.mixer.music.load(o[i])
                pygame.mixer.music.play()



    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            
    # Рендеринг
    screen.fill('white')

    pygame.time.delay(20)

pygame.quit()