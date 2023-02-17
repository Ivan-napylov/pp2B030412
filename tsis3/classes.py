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


Square(8, 2).area()
Rectangle(8, 2).area()