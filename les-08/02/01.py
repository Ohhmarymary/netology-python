# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionByZero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_zero(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return "на ноль делить нельзя"


divistion_numbers = DivisionByZero(4, 2)
print(DivisionByZero.divide_by_zero(234, 234))
print(DivisionByZero.divide_by_zero(60, 10))
print(divistion_numbers.divide_by_zero(4, 0))
