# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
# извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
# структуры на реальных данных.

class Date:

    def __init__(self, date: str):
        self.date = date

    @classmethod
    def transform_number(cls, date: str):
        date_parse = date.split("-")
        for date in date_parse:
            int(date)
        return int(date_parse[0]), int(date_parse[1]), int(date_parse[2])

    @staticmethod
    def validation_date(day: int, month: int, year: int):
        if 0 < int(day) < 31:
            if 0 < int(month) <= 12:
                if 0 < int(year) <= 9999:
                    return "формат числа, месяца и года верные!"
                else:
                    return "год неверного формата"
            else:
                return "месяц неверного формата"
        else:
            return "число неверного формата"


str_date = "32-09-2021"
print(Date.validation_date(13,12,-2))
print(Date.transform_number(str_date))
