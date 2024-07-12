from house import *

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
h4 = House('Домик в деревне', 1)
print(House.houses_history)

h1 += 10
print(h1)

h2 -= 10
print(h2)
h1 *= 2
print(h1)
h4 += 1
print(h4)
del h2
del h3

# Вывод списка - история изменений состояний объектов
print(House.houses_changes_history)
# Вывод изменений состояний всех объектов через метод Класса
print(House.get_changes_history(''))
# Вывод изменений ЖК Акация через метод Класса
print(House.get_changes_history('Акация'))
# Вывод изменений всех ЖК через метод Класса
print(House.get_changes_history('жк'))
# При указании несуществующего наименования выводится пустой список
print(House.get_changes_history('цыфй'))
