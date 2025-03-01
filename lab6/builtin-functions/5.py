def check(values):
    return all(values)
text = input().split()
values = tuple(
    True if item.lower() == 'true' else False if item.lower() == 'false' else int(item)
    for item in text
)
print(check(values))