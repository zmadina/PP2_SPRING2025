list = ['2','4','7']
with open("/Users/madinazangirova/Desktop/PP2_SPRING2025/lab6/dir-and-files/rrr.txt",'r') as f:
    for line in list:
        f.write(f"{line}\n")
        print(f"{line} write successful")