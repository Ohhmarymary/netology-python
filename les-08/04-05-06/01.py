# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Warehouse:

    def __init__(self):
        self.__storage = []

    def add(self, equipments):
        if not all([isinstance(equipment, OfficeEq) for equipment in equipments]):
            raise AddStorageError(f"Вы пытаетесь добавить на склад не оргтехнику")

        self.__storage.extend(equipments)

    def transfer(self, idx: int, department: str):
        item: OfficeEq = self.__storage[idx]
        if not isinstance(idx, int):
            raise TransferStorageError(f"Недопустимый тип '{type(item)}'")


        if item.department:
            raise TransferStorageError(f"Оборудование {item} уже закреплено за отделом {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for id_, item in enumerate(self):
            if all([item.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield id_, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__storage[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__storage[key]

    def __iter__(self):
        return self.__storage.__iter__()

    def __str__(self):
        return f"На складе сейчас {len(self.__storage)} устройств"


class OfficeEq:
    __required_props = ("eq_type", "vendor", "model")

    def __init__(self, eq_type: str = None, vendor: str = "", model: str = ""):
        self.type = eq_type
        self.vendor = vendor
        self.model = model

        self.department = None

    def __setattr__(self, key, value):
        if key in self.__required_props and not value:
            raise AttributeError(f"'{key}' должен иметь значение отличное от false")

        object.__setattr__(self, key, value)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"

    @staticmethod
    def validate(cnt):
        if not isinstance(cnt, int):
            ValidateEquipmentError(f"'{type(cnt)}'; количество инстансов должен быть типа 'int'")

    @classmethod
    def create(cls, cnt, **properties):
        cls.validate(cnt)
        return [cls(**properties) for _ in range(cnt)]


class AppError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AcceptStorageError(AppError):
    def __init__(self, text):
        self.text = f"Невозможно добавить товар на склад:\n {text}"


class TransferStorageError(AppError):
    def __init__(self, text):
        self.text = f"Ошибка прередачи оборудования:\n {text}"


AddStorageError = AcceptStorageError


class ValidateEquipmentError(AppError):
    pass


class Printer(OfficeEq):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Printer', **kwargs)


class Scanner(OfficeEq):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Scanner', **kwargs)


class Xerox(OfficeEq):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Xerox', **kwargs)


unit_1 = Printer('Toshiba', 123123, 13, 66)
unit_2 = Scanner('HP', 3131, 5, 33)
unit_3 = Xerox('Philips', 4242, 3, 22)
# print(unit_1.reception())
# print(unit_2.reception())
# print(unit_3.reception())
print(unit_1.to_print())
print(unit_2.to_scan())
print(unit_3.to_xerox())