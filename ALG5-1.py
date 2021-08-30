# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

import collections

def sum_tuple(numbers):

    total_sum = 0
    for sum_q in numbers:
        total_sum += sum_q
        return total_sum


Firma = collections.namedtuple('Firma', ['q1', 'q2', 'q3', 'q4'])

catalog_firm = {}

n = int(input("Number of firms : "))

for i in range(n):
    name = input(str(i+1) + ' Firm Name : ')
    profit_q1 = int(input('Q1 profit : '))
    profit_q2 = int(input('Q2 profit : '))
    profit_q3 = int(input('Q3 profit : '))
    profit_q4 = int(input('Q4 profit : '))
    catalog_firm[name] = Firma(
        q1=profit_q1,
        q2=profit_q2,
        q3=profit_q3,
        q4=profit_q4
    )

total_profit = ()

for name, profit in catalog_firm.items():
    print(f'Year profit for firm : {name} - {sum(profit)}')
    total_profit += profit

avg_profit_total = sum(total_profit) / len(catalog_firm)
print(f'Avg profit :  {avg_profit_total}')

print('Firms with profit higher than avg. :')

for name, profit in catalog_firm.items():
    if sum(profit) > avg_profit_total:
        print(f'{name} - {sum(profit)}')

print('Firms with profit below avg. :')

for name, profit in catalog_firm.items():
    if sum(profit) < avg_profit_total:
        print(f'{name} - {sum(profit)}')