import re
text= input()
pattern = r'а.*б'
result = re.findall(pattern, text)
print(result)