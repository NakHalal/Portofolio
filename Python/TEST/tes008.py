import re

s = input()

if re.match('[A-Za-z]', s):
    print(s)