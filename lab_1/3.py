import math
a = int(input())
b = int(input())
c = int(input())

if (c == int(math.sqrt(a ** 2 + b ** 2))):
    print("c is the triangle's hypotenuse")
else:
    print("c is not the triangle's hypotenuse")
