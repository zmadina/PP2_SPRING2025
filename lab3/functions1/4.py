def filter_prime(numbers):
    for x in numbers:
        if x > 1: 
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    break
            else:  
                print(x)
filter_prime([6, 3, 7])
