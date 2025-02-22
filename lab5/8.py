import re
text = input()
pattern = r'(?=[A-Z])'
result = re.split(pattern, text)
result = [x for x in result if x] 
print(result)
