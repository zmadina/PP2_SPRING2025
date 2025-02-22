import re
text= input()
pattern = r'[А-Я][а-я]+'
result = re.findall(pattern, text)
print(result)