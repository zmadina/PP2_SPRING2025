import re
text= input()
pattern = r'\b\w+_\w+\b'
result = re.findall(pattern, text)
print(result)