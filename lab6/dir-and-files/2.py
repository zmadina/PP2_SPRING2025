import os
def check_existence(path):
    if not os.path.exists(path):
        print("The specified path does not exist.")
        return
    else:
        print("The specified path exist")

def check_readwrite(path):
    fd = os.open(path, os.O_RDWR) 
    n = 3
    print(os.read(fd,n))
    print(os.write(fd, b"demo text"))
    os.close(fd)

path = input("Enter your path:")
check_existence(path)
check_readwrite(path)