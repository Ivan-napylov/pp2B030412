a = input()

b = a.split()

print("I have", end = " ")

for i in range (len(b)):
    if (i == len(b) - 1):
        print(b[i], end = " ")
    else:
        print(b[i], end = ", ")

print("in my shopping cart")