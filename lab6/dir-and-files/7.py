import os
with open("", 'r') as firstfile, open("", 'a') as secondfile:
    for line in firstfile:
        secondfile.write(line)