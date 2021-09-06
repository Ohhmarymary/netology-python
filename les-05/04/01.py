# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

translater = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
my_list = []

with open("1.txt", 'r') as file_obj:
    new_text = file_obj
    for text in new_text:
        text = text.split(" ", 1)
        my_list.append(translater[text[0]] + " " + text[1])

with open("2.txt", 'w') as file_obj:
    file_obj.writelines(my_list)