summary = 0
flag = True
while flag:
    userdata = input('введите несколько чисел, разделяя их пробелом').split(" ")
    for num in userdata:
        if num == "!":

            flag = False
            break
        elif num.isnumeric():
            summary += int(num)
    print(summary)