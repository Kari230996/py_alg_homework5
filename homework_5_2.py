'''
Практическая работа №5

Коллекции. Список. Очередь. Словарь.
'''

import collections

first = input('Введите 1-ое число в шестнадцатиричном формате: ').upper()
second = input('Введите 2-ое число в шестнадцатиричном формате: ').upper()

list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']

if len(first) > len(second):
  first, second = second, first


second = second[::-1]

third = collections.deque()


j = -1
k = 0
for i in second:
  one = list_of_numbers.index(i)
  two = list_of_numbers.index(first[j])
  third.append(list_of_numbers[(one + two + k) % 16])
  if (one + two) >= 15:
    k = 1
  else:
    k = 0
  j -= 1
  if j == -len(first)-1:
    break

diff = len(second) - len(first)

if diff:
    for i in second[-diff:]:
        third.append(list_of_numbers[(list_of_numbers.index(second[-diff]) + k) % 16])
        if list_of_numbers.index(second[-diff]) + 1 >= 15:
            k = 1
        else:
            k = 0
if k == 1:
  third.append('1')

third.reverse()

print(third)
