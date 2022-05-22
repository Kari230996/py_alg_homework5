'''
Практическая работа №5

Коллекции. Список. Очередь. Словарь.
'''

import collections

companies = collections.defaultdict()
big_avg = collections.deque()
litlle_avg = collections.deque()

n = int(input('Количество предприятия: '))

amount = 0

for i in range(1, n+1):
    name = input(f'\nВведите названия {i}-ого предприятия: ')
    quarter = 0
    profit = 0
    while quarter < 4:
        profit += float(input(f'Прибыль предприятия за {quarter+1}-квартал: '))
        quarter += 1

    companies[name] = profit
    amount += profit

print(companies)

avrg = amount / n

print(f"\nСредний доход всех предприятий за год составляет: {avrg}")

for i in companies:
    if companies[i] > avrg:
        big_avg.append(i)
    else:
        litlle_avg.append(i)


for i in big_avg:
    print(f'Предприятие с прибылем выше среднего: {i}')

for i in litlle_avg:
    print(f'Предприятие с прибылем ниже среднего: {i}')












