import os

def check_existence(path):
    if os.path.exists(path):
        directory = os.path.dirname(path)
        filename = os.path.basename(path)
        print(f"directory name {directory}")
        print(f"filename name {filename}")
        return
    else:
        print("The specified does not exist")
        return 

path = input()
check_existence(path)