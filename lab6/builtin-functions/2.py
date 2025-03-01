def count(text):
    lower = 0
    upper = 0
    for char in text:
        if char.islower():  
            lower += 1
        elif char.isupper(): 
            upper += 1
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)
text = input()
count(text)