def my_func(a, b, c):
    if a > b:
        if b > c:
            return a+b
        else:
            return a+c
        return a+c
    else:
        if a > c:
            return a + b
        else:
            return b + c


print("Сумма наибольших двух аргументов", my_func(5, 3, 4))
