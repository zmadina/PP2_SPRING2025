def even_nums(N):
    for i in range(N+1):
       if i%2==0:
           yield i
N = int(input())
evens = even_nums(N) 
print(", ".join(map(str, evens)))
