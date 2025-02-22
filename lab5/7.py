import re
def snake_to_camel(snake):
    def lower_to_upper(text):
        return text.group(1).upper()
    camel = re.sub(r"_(\w)", lower_to_upper, snake.lower())

    return camel
snake = input()
result= snake_to_camel(snake)
print(result)