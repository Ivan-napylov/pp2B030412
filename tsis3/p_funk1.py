def ounc():
    a = int(input("Write gramms: "))
    print (a * 28.3495231)

def Far():
    a = int(input("Write Fahrenheit temperature: "))
    print (5 / 9 * (a - 32))


def solve(numheads, numlegs):
    for i in range(numheads):
        if (i * 2 + (numheads - i) * 4) == numlegs:
            print("In farm we have {0} chickens and {1} rabbits".format(i, numheads - i))



def just():
    b = input("List: ")
    b = b.split(' ')
    a = []
    for i in b:
        if (int(i) == 2):
            a.append(int(i))
        elif (int(i) == 1 or int(i) == 0):
            pass
        else:
            v = True
            for j in range(2, int(i)):
                if (int(i) % j == 0):
                    v = False
                    break
            if (v):
                a.append(int(i))


    print(*a)

def str():
    a = input("String: ")
    a = a.split()
    for i in range(len(a) - 1, -1, -1):
        print(a[i])


def has_33(nums):
    for i in range(len(nums) - 1):
        if (nums[i] == 3 and nums[i + 1] == 3):
            print(True)
            break

def fly(nums):
    a = [0, 0, 7]
    b = 0
    for i in range(len(nums)):
        if (nums[i] == a[b]):
            b += 1
        
        if (b == 2):
            print("True")
            break


def rad():
    r = int(input("Radius: "))
    print(4 * 3.14 * r ** 3 / 3) 

def pal():
    a = input("STR: ")
    c = True

    for i in range(int(len(a) / 2)):
        if a[i] != a[len(a) - 1 - i]:
            c = False
            break
    
    if c:
        print(True)



def histogram(a):
    for i in range(len(a)):
        print("*" * a[i])


import random

def game():
    print("Hello! What is your name?")
    a = input()
    print()

    print("Well, {0}, I am thinking of a number between 1 and 20.".format(a))
    b = random.randint(0, 20)

    l = 0

    while(True):
        l += 1
        print("Take a guess.")
        c = int(input())
        print()
        if c == b:
            print("Good job, {0}! You guessed my number in {1} guesses!".format(a, l))
            break
        elif c < b:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

game()