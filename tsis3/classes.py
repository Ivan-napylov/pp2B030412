class Some():
    def __init__(self):
        self.a = ""
        
    def getSpring(self):
        self.a = input()

    def printString(self):
        print(self.a)

# Some().getSpring()
# Some().printString()


class Shape():
    def __init__(self, len, width):
        self.len = len
        self.width = width


class Square(Shape):
    def area(self):
        print((self.len)**2)

class Rectangle(Shape):
    def area(self):
        print(self.width * self.len)


# Square(8, 2).area()
# Rectangle(8, 2).area()


class Point():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def show(self):
        print("x : {0},    y: {1}".format(self.x, self.y))

    def move(self):
        self.x = int(input("New x:  "))
        self.y = int(input("New y:  "))

    def dist(self, x1, y1, x2, y2):
        print("Distance from first point: ", ((self.x - x1) ** 2 + (self.y - y1) ** 2) ** 0.5)
        print("Distance from second point: ", ((self.x - x2) ** 2 + (self.y - y2) ** 2) ** 0.5)


# p = Point(2, 4)
# p.show()
# p.dist(7, 8, 4, 5)



class Account():
    def __init__(self):
        pass

    def owner(self, name):
        self.name = name

    def balance(self, bal):
        self.bal = bal

    def deposit(self, mon):
        self.bal += mon

    def withdraw(self, mon):
        if (mon > self.bal):
            print("U can not do it, because u didn't have available balance")
        else:
            print("Your money: bzzzzzz")
            self.bal -= mon

# acc = Account()
# acc.owner("Ivan")
# acc.balance(800)
# acc.deposit(200)
# acc.withdraw(1000)


class filter():
    def __init__(self, list):
        self.list = list
        x = []
        for i in range(len(self.list)):
            k = True
            for j in range(2, self.list[i]):
                if (self.list[i] % j == 0):
                    k = False
                    break
            if (k):
                x.append(self.list[i])

        print(x)


filter([7, 8, 9, 10, 11, 12, 13])
            