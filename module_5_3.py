from house import *

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)
h1 = h1 + 10
print(h1)
print(h1 == h2)

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)

print(hash(h1))
print(hash(h2))
print(hash(30))

print(h1 / 3.55)
print(h1*2.5)
print(h1+h2) ## в данном случае операция не выполяется, поскольку h2 не является int или float