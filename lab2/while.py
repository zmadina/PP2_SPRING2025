i = 1
while i < 9:
  print(i)
  i += 1


q = 1
while q < 4:
  print(q)
  if q == 2:
    break
  q += 1


j = 0
while j < 5:
  j += 1
  if j == 3:
    continue
  print(j)


o = 1
while o < 6:
  print(o)
  o += 1
else:
  print("o is no longer less than 6")