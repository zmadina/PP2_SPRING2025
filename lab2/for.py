for x in "cap":
  print(x)


nature = ["trees", "river", "bear"]
for x in nature:
  if x == "river":
    break
  print(x)


cat = ["paw", "tail", "whiskers"]
for x in cat:
  if x == "paw":
    continue
  print(x)


for x in range(2, 10, 3):
  print(x) 


for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


adj = ["blue", "pink", "yellow"]
flowers = ["roses", "gypsophilas", "peonies"]

for x in adj:
  for y in flowers:
    print(x, y)


for x in [0, 1, 2]:
  pass