# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('1.txt', 'r') as file_obj:
    new_text = file_obj.read().split('\n')

    lines = len(new_text)
    lines_number = 0
    len_words = 0
    for text in new_text:
        lines_number += 1
        len_words = len(text)
        print(f"в строчке №{lines_number} столько символов — {len_words}")

    print(f"всего в файле {len(new_text)} строч.")
