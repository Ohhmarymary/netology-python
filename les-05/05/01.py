# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

try:
    with open("01.txt", "w") as file_obj:
        numbers = input('введите числа через пробел')
        file_obj.writelines(str(numbers))
        print(sum(map(int, numbers.split())))
except IOError:
    print('ошибка файла')
except ValueError:
    print("ошибка значений")
