class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.current_floor = 1

    def __str__(self):
        return f'{self.name} имеет {self.number_of_floors} этажей'

    @property
    def __hash__(self):
        return hash(self.name, str(self.number_of_floors))

    def __len__(self):
        return self.number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Ошибка. Такого этажа не существует')
            return
        else:
            for i in range(1, new_floor + 1):
                print(f'Этаж : {i} ')

    def lift(self, new_floor):
        print(f'Лифт находится на этаже : {self.current_floor} ')
        if new_floor < 1:
            print('Ошибка. Такого этажа не существует. Двигаемся на самый нижний этаж')
            new_floor = 1
        if new_floor > self.number_of_floors:
            print('Ошибка. Такого этажа не существует. Двигаемся на самый верхний этаж')
            new_floor = self.number_of_floors
        if new_floor > self.current_floor:
            for i in range(self.current_floor + 1, new_floor + 1):
                print(f'Этаж : {i} ')
        elif new_floor < self.current_floor:
            for i in range(self.current_floor - 1, new_floor - 1, -1):
                print(f'Этаж : {i} ')
        else:
            print(f'Лифт стоит на месте. Этаж {self.current_floor}')
            return
        self.current_floor = new_floor
        print(f'Лифт приехал на этаж : {self.current_floor} ')


house_1 = House('ЖК Горский', 18)
house_2 = House('Домик в деревне', 2)
house_1.go_to(5)
house_2.go_to(10)

house_1.lift(3)
house_1.lift(-3)
house_1.lift(17)
house_1.lift(12)
house_1.lift(12)
house_1.lift(25)

house_3 = House('ЖК Эльбрус', 10)
house_4 = House('ЖК Акация', 20)
print(house_1)
print(len(house_1))
print(house_2)
print(len(house_2))
print(house_3)
print(len(house_3))
print(house_4)
print(len(house_4))
