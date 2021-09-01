# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
import argparse
import salary

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('time', type=float)
parser.add_argument('rate', type=float)
parser.add_argument('prize', type=float)

args = parser.parse_args(argv[1:])

print(salary.calculate(float(args.time), float(args.rate), float(args.prize)))
