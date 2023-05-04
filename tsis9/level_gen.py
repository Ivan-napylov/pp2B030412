<<<<<<< HEAD
import random
width = 40
height = 30
matrix = [["0" for j in range(width)] for i in range(height)]
walls = 900

def pp(a):
    for i in range(len (a)):
        for j in range(len (a[i])):
            print((a[i][j]), end=" ")
        print()

for i in range(walls):
    matrix[random.randint(0, height-1)][random.randint(0, width - 1)] = "$"


pp(matrix)


f = open('5.txt', 'w')


for i in range(height):
    str = ""
    for j in range(width):
        str += matrix[i][j]
    f.write(str + '\n')

f.close()

=======
import random
width = 40
height = 30
matrix = [["0" for j in range(width)] for i in range(height)]
walls = 900

def pp(a):
    for i in range(len (a)):
        for j in range(len (a[i])):
            print((a[i][j]), end=" ")
        print()

for i in range(walls):
    matrix[random.randint(0, height-1)][random.randint(0, width - 1)] = "$"


pp(matrix)


f = open('5.txt', 'w')


for i in range(height):
    str = ""
    for j in range(width):
        str += matrix[i][j]
    f.write(str + '\n')

f.close()

>>>>>>> 985e77223eb5e18e20bef0d61673810c19912873
