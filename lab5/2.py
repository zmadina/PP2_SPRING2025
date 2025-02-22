import re
text= input()
pattern = r'аб{1,3}'
result = re.findall(pattern, text)
print(result)