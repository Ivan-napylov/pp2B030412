import pygame
from datetime import datetime


pygame.init()
pygame.display.set_caption("Game")

screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()



image = pygame.transform.scale(pygame.image.load('graphics/mickey_head.png').convert_alpha(), (300, 300))
cl_im = pygame.transform.scale(pygame.image.load('graphics/clock.png').convert_alpha(), (640, 640))
r = pygame.transform.scale(pygame.image.load('graphics/hand.png').convert_alpha(), (640, 640))
l = pygame.transform.scale(pygame.image.load('graphics/long.png').convert_alpha(), (640, 640))


running = True

s = int(datetime.now().strftime("%S")) * 6
m = int(datetime.now().strftime("%M")) * 30


while running:
    print(datetime.now().strftime("%S"), datetime.now().strftime("%M"))


    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            
    # Рендеринг
    screen.fill('white')


    screen.blit(image, (170, 110))
    screen.blit(cl_im, (0, 0))



    rot_r = pygame.transform.rotate(r, -s)
    s += 0.06
    rot_r_r = rot_r.get_rect(center = r.get_rect(topleft = (0, 0)).center)

    screen.blit(rot_r, rot_r_r)


    rot_l = pygame.transform.rotate(l, -m)
    m += 0.012
    rot_l_r = rot_l.get_rect(center = l.get_rect(topleft = (0, 0)).center)

    screen.blit(rot_l, rot_l_r)


    t = datetime.now()
    pygame.display.update()

    clock.tick(100)

pygame.quit()