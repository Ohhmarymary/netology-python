def test(number1, number2):
    if number2 == 0:
        print('делить на ноль нельзя!')
    else:
        return number1/number2


a = int(input('какое число будем делить?'))
b = int(input('на какое число будем делить?'))
print(test(a, b))

