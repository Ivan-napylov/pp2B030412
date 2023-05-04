import os
# fpath = 'C:/Users/User/Desktop/PP2'

# for dirpath, dirnames, filenames in os.walk(fpath):
#     print("directory:", dirpath)
#     print("subdirectories:", dirnames)
#     print("files:", filenames)
#     print()


#================================================================
#================================================================

# fpath = 'C:/Users/User/Desktop/PP3'

# if not os.path.exists(fpath):
#     print("Not exist")
# else:
#     print("Exist")

#================================================================
#================================================================

# fpath = 'C:/Users/User/Desktop/PPs2'

# if not os.path.exists(fpath):
#     print("Not exist")
# else:
#     for dirpath, dirnames, filenames in os.walk(fpath):
#         print("directory:", dirpath)
#         print("subdirectories:", dirnames)
#         print("files:", filenames)
#         print()


#================================================================
#================================================================

# c = 0
# import utils

# text = utils.read_file('row.txt')

# for line in text:
#     c += 1

# print(c)

#================================================================
#================================================================

# import string


# letters = string.ascii_uppercase

# for i in letters:
#     with open(i + ".txt", "w") as f:
#         f.write(i)


#================================================================
#================================================================

a = ''

with open("A.txt", 'r') as f:
    a = f.read()

with open("B.txt", 'w') as f:
    f.write(a)


#================================================================
#================================================================


# fpath = 'C:/Users/User/Desktop/PP2/tsis6/row.txt'

# if not os.path.exists(fpath):
#     print("Not exist")
# else:
#     os.remove('C:/Users/User/Desktop/PP2/tsis6/row.txt')