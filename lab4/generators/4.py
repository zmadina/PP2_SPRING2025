def squares(a,b):
    for i in range(a,b+1):
       yield i*i
a=int(input())
b=int(input())
nums = squares(a,b) 
for num in nums:
    print(num)