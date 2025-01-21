x = "great"

def myfunc():
    print("KBTU is " + x)

myfunc()

y = "cute"

def lol():
    global y
    y = "crazy"  
    print("She is kinda " + y)

lol()

print("She is kinda " + y)

def sus():
    global z
    z = "angelic"

sus()

print("His voice is " + z)

f = "angelic"

def bark():
    global x 
    x = "normal"  

bark()

print("His voice is " + x)
