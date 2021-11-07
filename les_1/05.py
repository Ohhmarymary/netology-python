income = int(input('Введите выручку'))
cost = int(input('Введите издержки'))

if income > cost:
    result = "in"
    print('Фирма работает прибыльно')
    profit = income - cost
    profitability = profit/income
    print('рентабельность фирмы составляет', profitability)
    employee = int(input('сколько сотрудников работает в вашей фирме'))
    profit_person = profit/employee
    print('прибыль на одного сотрудника составляет', int(profit_person))
else:
    result = "cost"
    print('Фирма работает в убыток')

