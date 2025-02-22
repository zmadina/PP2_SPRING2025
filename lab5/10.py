import re
def camel_to_snake(camel):
    snake = re.sub(r'([A-Z])',r'_\1', camel).lower() 
    return snake
camel = input()
result= camel_to_snake(camel)
print(result)