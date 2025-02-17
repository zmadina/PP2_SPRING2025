def div_nums(N):
    for i in range(N+1):
       if i%3==0 and i%4==0:
           yield i
N = int(input())
nums = div_nums(N) 
for num in nums:
    print(num)