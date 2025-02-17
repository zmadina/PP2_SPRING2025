def square_nums(N):
    for i in range(1, N+1):
        yield(i*i)
N = int(input())
squares = square_nums(N) 
for square in squares:
    print(square)

