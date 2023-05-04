<<<<<<< HEAD
import collections

import pygame

pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)


# Point = collections.namedtuple('Point', ['x', 'y'])

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GameObject:
    def draw(self):
        return

    def update(self, current_pos):
        return


class Button(GameObject):
    def __init__(self, color, shape, x):
        self.size = 40
        self.color = color
        self.x = x
        self.rect = pygame.draw.rect(
            SCREEN,
            self.color,
            (
                # WIDTH // 2 - self.size // 2,
                self.x,
                20,
                self.size,
                self.size,
            )
        )
        self.connected_shape = shape

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            self.color,
            (
                self.x,
                20,
                self.size,
                self.size,
            )
        )

    def update(self, current_pos):
        pass


class Pen(GameObject):
    def __init__(self, *args, **kwargs):  # Pen(1, 2, 3, a=4) =>
        self.points: list[Point] = []  # [(x1, y1), (x2, y2)]

    def draw(self):
        for idx, point in enumerate(self.points[:-1]):  # range(len(self.points))
            next_point = self.points[idx + 1]
            pygame.draw.line(
                SCREEN,
                WHITE,
                start_pos=(point.x, point.y),  # self.points[idx]
                end_pos=(next_point.x, next_point.y),
                width=5
            )

    def update(self, current_pos):
        self.points.append(Point(*current_pos))  # (x, y) Point((x, y)) => Point(x, y)



class Rectangle(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.rect(
            SCREEN,
            WHITE,
            (
                start_pos_x, start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class Circle(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.ellipse(
            SCREEN,
            WHITE,
            (
                start_pos_x, start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            )
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class Square(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)
        

        if (end_pos_y - start_pos_y > end_pos_x - start_pos_x):
            pygame.draw.polygon(
            SCREEN,
            WHITE,
            [[start_pos_x, start_pos_y], [start_pos_x + end_pos_y - start_pos_y, start_pos_y], [start_pos_x + end_pos_y - start_pos_y, end_pos_y], [start_pos_x, end_pos_y]],
            width=5,
        )
        else:
            pygame.draw.polygon(
            SCREEN,
            WHITE,
            [[start_pos_x, start_pos_y], [end_pos_x, start_pos_y], [end_pos_x, start_pos_y + end_pos_x - start_pos_x], [start_pos_x, start_pos_y + end_pos_x - start_pos_x]],
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class R_trian(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.polygon(
            SCREEN,
            WHITE, [[start_pos_x, start_pos_y], [end_pos_x, end_pos_y], [end_pos_x, start_pos_y]],
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos


class Eq_tr(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.polygon(
            SCREEN,
            WHITE, [[start_pos_x, start_pos_y], [start_pos_x + int((end_pos_x - start_pos_x)/2), start_pos_y + int((end_pos_x - start_pos_x) / 2 * 1.732)], [end_pos_x, start_pos_y]],
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos


class Romb(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.polygon(
            SCREEN,
            WHITE, [[start_pos_x, start_pos_y + int((end_pos_y - start_pos_y)/2)], [start_pos_x + int((end_pos_x - start_pos_x)/2), start_pos_y], [end_pos_x, start_pos_y + int((end_pos_y - start_pos_y)/2)], [start_pos_x + int((end_pos_x - start_pos_x)/2), end_pos_y]],
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos


def main():
    running = True
    game_object = GameObject()
    active_obj = game_object
    current_shape = Pen  # current_shape()
    buttonrect = Button((0, 255, 0), Rectangle, WIDTH // 2 - 20)
    buttonpen = Button((0, 255, 255), Pen, WIDTH // 2 - 70)
    buttoncircle = Button((255, 255, 0), Circle, WIDTH // 2 - 120)
    buttonsq = Button((125, 124, 124), Square, WIDTH // 2 - 170)
    button_r_trian = Button((0, 125, 0), R_trian, WIDTH // 2 + 30)
    button_eq_tr = Button((125, 0, 0), Eq_tr, WIDTH // 2 + 80)
    button_romb = Button((0, 0, 125), Romb, WIDTH // 2 + 130)
    objects = [
        buttonrect,
        buttonpen,
        buttoncircle,
        buttonsq,
        button_r_trian,
        button_eq_tr,
        button_romb
    ]

    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttonrect.rect.collidepoint(event.pos):
                    current_shape = buttonrect.connected_shape

                elif buttonpen.rect.collidepoint(event.pos):
                    current_shape = buttonpen.connected_shape

                elif buttoncircle.rect.collidepoint(event.pos):
                    current_shape = buttoncircle.connected_shape

                elif buttonsq.rect.collidepoint(event.pos):
                    current_shape = buttonsq.connected_shape
                
                elif button_r_trian.rect.collidepoint(event.pos):
                    current_shape = button_r_trian.connected_shape

                elif button_eq_tr.rect.collidepoint(event.pos):
                    current_shape = button_eq_tr.connected_shape

                elif button_romb.rect.collidepoint(event.pos):
                    current_shape = button_romb.connected_shape
                
                else:
                    active_obj = current_shape(start_pos=event.pos)
                    objects.append(active_obj)

            if event.type == pygame.MOUSEMOTION:
                active_obj.update(current_pos=pygame.mouse.get_pos())

            if event.type == pygame.MOUSEBUTTONUP:
                active_obj = game_object

        for obj in objects:
            obj.draw()

        clock.tick(30)
        pygame.display.flip()


if __name__ == '__main__':
=======
import collections

import pygame

pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)


# Point = collections.namedtuple('Point', ['x', 'y'])

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GameObject:
    def draw(self):
        return

    def update(self, current_pos):
        return


class Button(GameObject):
    def __init__(self, color, shape, x):
        self.size = 40
        self.color = color
        self.x = x
        self.rect = pygame.draw.rect(
            SCREEN,
            self.color,
            (
                # WIDTH // 2 - self.size // 2,
                self.x,
                20,
                self.size,
                self.size,
            )
        )
        self.connected_shape = shape

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            self.color,
            (
                self.x,
                20,
                self.size,
                self.size,
            )
        )

    def update(self, current_pos):
        pass


class Pen(GameObject):
    def __init__(self, *args, **kwargs):  # Pen(1, 2, 3, a=4) =>
        self.points: list[Point] = []  # [(x1, y1), (x2, y2)]

    def draw(self):
        for idx, point in enumerate(self.points[:-1]):  # range(len(self.points))
            next_point = self.points[idx + 1]
            pygame.draw.line(
                SCREEN,
                WHITE,
                start_pos=(point.x, point.y),  # self.points[idx]
                end_pos=(next_point.x, next_point.y),
                width=5
            )

    def update(self, current_pos):
        self.points.append(Point(*current_pos))  # (x, y) Point((x, y)) => Point(x, y)



class Rectangle(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.rect(
            SCREEN,
            WHITE,
            (
                start_pos_x, start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class Circle(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.ellipse(
            SCREEN,
            WHITE,
            (
                start_pos_x, start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            )
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class Square(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)
        

        if (end_pos_y - start_pos_y > end_pos_x - start_pos_x):
            pygame.draw.polygon(
            SCREEN,
            WHITE,
            [[start_pos_x, start_pos_y], [start_pos_x + end_pos_y - start_pos_y, start_pos_y], [start_pos_x + end_pos_y - start_pos_y, end_pos_y], [start_pos_x, end_pos_y]],
            width=5,
        )
        else:
            pygame.draw.polygon(
            SCREEN,
            WHITE,
            [[start_pos_x, start_pos_y], [end_pos_x, start_pos_y], [end_pos_x, start_pos_y + end_pos_x - start_pos_x], [start_pos_x, start_pos_y + end_pos_x - start_pos_x]],
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class R_trian(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.polygon(
            SCREEN,
            WHITE, [[start_pos_x, start_pos_y], [end_pos_x, end_pos_y], [end_pos_x, start_pos_y]],
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos


class Eq_tr(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.polygon(
            SCREEN,
            WHITE, [[start_pos_x, start_pos_y], [start_pos_x + int((end_pos_x - start_pos_x)/2), start_pos_y + int((end_pos_x - start_pos_x) / 2 * 1.732)], [end_pos_x, start_pos_y]],
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos


class Romb(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.polygon(
            SCREEN,
            WHITE, [[start_pos_x, start_pos_y + int((end_pos_y - start_pos_y)/2)], [start_pos_x + int((end_pos_x - start_pos_x)/2), start_pos_y], [end_pos_x, start_pos_y + int((end_pos_y - start_pos_y)/2)], [start_pos_x + int((end_pos_x - start_pos_x)/2), end_pos_y]],
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos


def main():
    running = True
    game_object = GameObject()
    active_obj = game_object
    current_shape = Pen  # current_shape()
    buttonrect = Button((0, 255, 0), Rectangle, WIDTH // 2 - 20)
    buttonpen = Button((0, 255, 255), Pen, WIDTH // 2 - 70)
    buttoncircle = Button((255, 255, 0), Circle, WIDTH // 2 - 120)
    buttonsq = Button((125, 124, 124), Square, WIDTH // 2 - 170)
    button_r_trian = Button((0, 125, 0), R_trian, WIDTH // 2 + 30)
    button_eq_tr = Button((125, 0, 0), Eq_tr, WIDTH // 2 + 80)
    button_romb = Button((0, 0, 125), Romb, WIDTH // 2 + 130)
    objects = [
        buttonrect,
        buttonpen,
        buttoncircle,
        buttonsq,
        button_r_trian,
        button_eq_tr,
        button_romb
    ]

    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttonrect.rect.collidepoint(event.pos):
                    current_shape = buttonrect.connected_shape

                elif buttonpen.rect.collidepoint(event.pos):
                    current_shape = buttonpen.connected_shape

                elif buttoncircle.rect.collidepoint(event.pos):
                    current_shape = buttoncircle.connected_shape

                elif buttonsq.rect.collidepoint(event.pos):
                    current_shape = buttonsq.connected_shape
                
                elif button_r_trian.rect.collidepoint(event.pos):
                    current_shape = button_r_trian.connected_shape

                elif button_eq_tr.rect.collidepoint(event.pos):
                    current_shape = button_eq_tr.connected_shape

                elif button_romb.rect.collidepoint(event.pos):
                    current_shape = button_romb.connected_shape
                
                else:
                    active_obj = current_shape(start_pos=event.pos)
                    objects.append(active_obj)

            if event.type == pygame.MOUSEMOTION:
                active_obj.update(current_pos=pygame.mouse.get_pos())

            if event.type == pygame.MOUSEBUTTONUP:
                active_obj = game_object

        for obj in objects:
            obj.draw()

        clock.tick(30)
        pygame.display.flip()


if __name__ == '__main__':
>>>>>>> 985e77223eb5e18e20bef0d61673810c19912873
    main()