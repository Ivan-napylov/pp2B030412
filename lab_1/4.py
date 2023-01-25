num = int(input())
str = input()

if(str.isdigit()):
    str = int(str)
    print(str % num)

else:
    print(str * num)