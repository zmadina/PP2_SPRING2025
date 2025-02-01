mylist = ['tea', 'coffee', 'kakao']
print(mylist[1])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


lilist = ["tv", "radio", "computer"]
lilist[1:3] = ["phone"]
print(lilist)


average = ["pear", "banana", "lemon"]
tropical = ["mango", "pineapple", "papaya"]
average.extend(tropical)
print(average)


lololo = ["eyes", "lips", "nose"]
del lololo[0]
print(lololo)


sky = ["moon", "star", "sun"]
i = 0
while i < len(sky):
  print(sky[i])
  i = i + 1


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


tomatoma = ["aruzhan", "tomiris", "madina", "ayana" ]
tomatoma.reverse()
print(tomatoma)


bakery = ["cake", "muffin", "cookie"]
pastry = bakery.copy()
print(pastry)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)


points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
c = points.count(9)
print(c)











