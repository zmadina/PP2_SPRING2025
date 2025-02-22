import re
def wsub(text):
    return re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
text = input()
result = wsub(text)
print(result)