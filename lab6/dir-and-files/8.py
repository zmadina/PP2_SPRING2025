
import os
def check_path(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("The file does not exist")

path = input()
check_path(path)