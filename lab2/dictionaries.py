dicot = {
  "brand": "Tesla",
  "model": "X",
  "year": 2018
}
print(type(dicot))


birds= {
  "type": "dove",
  "name": "lola",
  "year": 2023
}
x = birds["type"]
print(x)


nomnom = {
  "type": "pasta",
  "name": "Alfredo",
  "year": 2024
}
nomnom.update({"year": 2025})
print(nomnom)


car = {
  "brand": "Chevrolet",
  "model": "Cobalt",
  "year": 2023
}
car["color"] = "white"
print(car)


clothes = {
  "brand": "Bershka",
  "element": "skirt",
  "price": 19000
}
del clothes["price"]
print(clothes)
for x in clothes:
  print(clothes[x])
  


swtreat = {
  "type": "icecream",
  "flavour": "pistachio",

}
mytreat = dict(swtreat)
print(mytreat)


pet1 = {
  "name" : "Tom",
  "type" : "cat"
}
pet2 = {
  "name" : "Rex",
  "type" : "dog"
}
pet3 = {
  "name" : "Nemo",
  "type" : "fish"
}
mypets = {
  "pet1" : pet1,
  "pet2" : pet2,
  "pet3" : pet3
}
print(mypets)







