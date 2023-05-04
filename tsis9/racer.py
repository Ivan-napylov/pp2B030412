<<<<<<< HEAD
import random

import pygame

pygame.init()
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
SCORE = 0
clock = pygame.time.Clock()
background = pygame.image.load('./materials/AnimatedStreet.png')
score_font = pygame.font.SysFont("Verdana", 30)
#


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.image = pygame.image.load('./materials/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(self.rect.width, WIDTH - self.rect.width),
            0,
        )

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if self.rect.y > HEIGHT:
            SCORE += 1
            self.speed += 1
            self.rect.center = (
                random.randint(self.rect.width, WIDTH - self.rect.width),
                0,
            )


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.image = pygame.image.load('./materials/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.x - self.speed >= 0:
            self.rect.move_ip(-self.speed, 0)
        elif pressed[pygame.K_RIGHT] and self.rect.x + self.speed + self.rect.width <= WIDTH:
            self.rect.move_ip(self.speed, 0)

    



class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 2
        self.score = random.randint(1, 10)
        print(self.score)
        self.image = pygame.transform.scale(pygame.image.load('./materials/Coin.png').convert_alpha(), (self.score * 5, self.score * 5))
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(self.rect.width, WIDTH - self.rect.width),
            0,
        )

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, x, y, h, w):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if (self.rect.y > HEIGHT) or (self.rect.y + 50 > y and self.rect.y + 50 < y + h and self.rect.x + 25 > x and self.rect.x + 25 < x + w):
            SCORE += self.score
            self.speed += 1
            self.rect.center = (
                random.randint(self.rect.width, WIDTH - self.rect.width),
                0,
            )
            self.score = random.randint(0, 10)
            self.image = pygame.transform.scale(pygame.image.load('./materials/Coin.png').convert_alpha(), (self.score * 5, self.score * 5))
def main():
    running = True
    player = Player()
    enemy = Enemy()
    coin = Coin()
    enemies = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    coins.add(coin)
    enemies.add(enemy)
    global i
    i = 1

    while running:
        # SCREEN.fill(WHITE)
        SCREEN.blit(background, (0, 0))
        score = score_font.render(f" Your score: {SCORE: }", True, (0, 0, 0))
        SCREEN.blit(score, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if SCORE > 15 * i:
            i += 1
            enemies.add(Enemy())


        player.update()
        coin.update(player.rect.x, player.rect.y, 96, 44)

        player.draw(SCREEN)
        coin.draw(SCREEN)
    
        for e in enemies:
            e.update()
            e.draw(SCREEN)

        if pygame.sprite.spritecollideany(player, enemies):
            running = False

        if pygame.sprite.spritecollideany(player, coins):
            coin.update(player.rect.x, player.rect.y, 96, 44)

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
=======
import random

import pygame

pygame.init()
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
SCORE = 0
clock = pygame.time.Clock()
background = pygame.image.load('./materials/AnimatedStreet.png')
score_font = pygame.font.SysFont("Verdana", 30)
#


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.image = pygame.image.load('./materials/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(self.rect.width, WIDTH - self.rect.width),
            0,
        )

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if self.rect.y > HEIGHT:
            SCORE += 1
            self.speed += 1
            self.rect.center = (
                random.randint(self.rect.width, WIDTH - self.rect.width),
                0,
            )


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.image = pygame.image.load('./materials/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.x - self.speed >= 0:
            self.rect.move_ip(-self.speed, 0)
        elif pressed[pygame.K_RIGHT] and self.rect.x + self.speed + self.rect.width <= WIDTH:
            self.rect.move_ip(self.speed, 0)

    



class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 2
        self.score = random.randint(1, 10)
        print(self.score)
        self.image = pygame.transform.scale(pygame.image.load('./materials/Coin.png').convert_alpha(), (self.score * 5, self.score * 5))
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(self.rect.width, WIDTH - self.rect.width),
            0,
        )

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, x, y, h, w):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if (self.rect.y > HEIGHT) or (self.rect.y + 50 > y and self.rect.y + 50 < y + h and self.rect.x + 25 > x and self.rect.x + 25 < x + w):
            SCORE += self.score
            self.speed += 1
            self.rect.center = (
                random.randint(self.rect.width, WIDTH - self.rect.width),
                0,
            )
            self.score = random.randint(0, 10)
            self.image = pygame.transform.scale(pygame.image.load('./materials/Coin.png').convert_alpha(), (self.score * 5, self.score * 5))
def main():
    running = True
    player = Player()
    enemy = Enemy()
    coin = Coin()
    enemies = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    coins.add(coin)
    enemies.add(enemy)
    global i
    i = 1

    while running:
        # SCREEN.fill(WHITE)
        SCREEN.blit(background, (0, 0))
        score = score_font.render(f" Your score: {SCORE: }", True, (0, 0, 0))
        SCREEN.blit(score, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if SCORE > 15 * i:
            i += 1
            enemies.add(Enemy())


        player.update()
        coin.update(player.rect.x, player.rect.y, 96, 44)

        player.draw(SCREEN)
        coin.draw(SCREEN)
    
        for e in enemies:
            e.update()
            e.draw(SCREEN)

        if pygame.sprite.spritecollideany(player, enemies):
            running = False

        if pygame.sprite.spritecollideany(player, coins):
            coin.update(player.rect.x, player.rect.y, 96, 44)

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
>>>>>>> 985e77223eb5e18e20bef0d61673810c19912873
    main()