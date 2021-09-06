# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
my_list = []

while True:
    text = input('Введите что-нибудь')
    if text == '':
        exit()
    else:
        new_text = text + '\n'
        my_list.append(new_text)

        with open('1.txt', 'w') as file_obj:
            file_obj.writelines(my_list)
