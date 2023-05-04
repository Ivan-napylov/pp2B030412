import re

import utils

def reg(pattern, path):
    with open(path, mode='r', encoding='utf8') as f:

        for line in f:
            matching = re.search(pattern, line)
            if matching is not None:
                print(line)



#================================================================
#================================================================

# reg(r'ДУ*', 'row.txt')

#================================================================
#================================================================

# reg(r'3{2,3}1', 'row.txt')


#================================================================
#================================================================

# reg(r'\w-\w', 'row.txt')

#================================================================
#================================================================

# reg(r'[А-Я]-[а-я]', 'row.txt')

#================================================================
#================================================================

# reg(r'С\bь', 'row.txt')

#================================================================
#================================================================

# string = "osdhf   asdlfkjasdlfn  asdfaksdf,.,.,., asdkfjn.,. dsa fasdkf as,d.,f .asd, f.as df, ads f"


# pattern = r'[\s,.]'
# print(re.sub(pattern, ':', string))


#================================================================
#================================================================


string = "osdhf___asdlfkjasdlfn__asdfaksdf________asdkfjn____dsa_fasdkf_as_d__f__asd__f_as_df__ads_f"


pattern = r'_'
print(re.sub(pattern, 'A', string))


#================================================================
#================================================================

# string = "osdhfAAAasdlfkjasdlfnAAasdfaksdfAAAAAAAAasdkfjnAAAAdsaAfasdkfAasAdAAfAAasdAAfAasAdfAAadsAf"


# pattern = r'[A - Z]+'
# list = re.split(pattern, string)

# a = ""
# for i in list:
#     a += i
#     a += " "

# print(a)

#================================================================
#================================================================


# string = "osdhf asdlfkjasdlfn asdfaksdf asdkfjn dsa fasdkf as d f asd f as df ads f"


# pattern = r'\s+'
# list1 = re.sub(r'\b\w', lambda m: m.group().upper(), string)
# list2 = re.sub(pattern, '', list1)

# print(list2)


#================================================================
#================================================================

# string = "osdhfAAAasdlfkjasdlfnAAasdfaksdfAAAAAAAAasdkfjnAAAAdsaAfasdkfAasAdAAfAAasdAAfAasAdfAAadsAf"


# pattern = r'[A - Z]'
# print(re.sub(pattern, '_', string))