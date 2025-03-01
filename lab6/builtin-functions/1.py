def multiply(numbers):
    result = 1  
    for num in numbers:
        result *= num  
    return result

numbers = list(map(int, input().split()))
print(multiply(numbers))