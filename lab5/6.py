import re
text= input()
pattern = r'[ ,.]' 
result = re.sub(pattern, ":", text)
print(result)