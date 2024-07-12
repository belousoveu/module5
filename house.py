class House:
    houses_history = []
    houses_changes_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        cls.houses_changes_history.append(("Создание нового дома", *args))
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.current_floor = 1

    def __str__(self):
        return f'{self.name} имеет {self.number_of_floors} этажей'

    def __hash__(self):
        return hash(self.number_of_floors)

    def __len__(self):
        return self.number_of_floors

    def __del__(self):
        self.houses_changes_history.append(("Снос дома", self.name, 0))
        print(f'Дом {self.name} был снесен, но останется в истории')

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
        else:
            return False

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.number_of_floors = int(self.number_of_floors + other)
            self.__class__.houses_changes_history.append(("Реконструкция дома", self.name, self.number_of_floors))
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.number_of_floors = int(self.number_of_floors - other)
            self.__class__.houses_changes_history.append(("Реконструкция дома", self.name, self.number_of_floors))
        return self

    def __isub__(self, other):
        return self.__sub__(other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.number_of_floors = int(self.number_of_floors * other)
            self.__class__.houses_changes_history.append(("Реконструкция дома", self.name, self.number_of_floors))
        return self

    def __imul__(self, other):
        return self.__mul__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.number_of_floors = int(self.number_of_floors / other)
            self.__class__.houses_changes_history.append(("Реконструкция дома", self.name, self.number_of_floors))
        return self

    def __itruediv__(self, other):
        return self.__truediv__(other)

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __floordiv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.number_of_floors = int(self.number_of_floors // other)
            self.__class__.houses_changes_history.append(("Реконструкция дома", self.name, self.number_of_floors))
        return self

    def __ifloordiv__(self, other):
        return self.__floordiv__(other)

    def __rfloordiv__(self, other):
        return self.__floordiv__(other)

    def __mod__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.number_of_floors = int(self.number_of_floors % other)
            self.__class__.houses_changes_history.append(("Реконструкция дома", self.name, self.number_of_floors))
        return self

    def __imod__(self, other):
        return self.__mod__(other)

    def __rmod__(self, other):
        return self.__mod__(other)

    def __pow__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.number_of_floors = int(self.number_of_floors ** other)
            self.__class__.houses_changes_history.append(("Реконструкция дома", self.name, self.number_of_floors))
        return self

    def __ipow__(self, other):
        return self.__pow__(other)

    def __rpow__(self, other):
        return self.__pow__(other)

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other
        else:
            return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other
        else:
            return False

    def __ne__(self, other):
        return not self == other

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

    @classmethod
    def get_changes_history(cls, name=''):
        changes_history = [x for x in cls.houses_changes_history if name.lower() in x[1].lower()]
        return changes_history
