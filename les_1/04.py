n = input('Введите целое положительное число')
higherNumber = 0
number = 0
while number < 10:
    result = str(number) in n
    if result:
        higherNumber = number
    number = number + 1
print("Самая большая цифра", higherNumber)
