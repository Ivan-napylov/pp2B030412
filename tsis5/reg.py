import re

import utils

text = utils.read_file('row.txt')


pattern = r'С[т]*'

for line in text:
    if re.search(pattern, line):
        print(line.strip())




