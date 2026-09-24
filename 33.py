n = int(input())
c = int(input())
k = int(input())

per_page = n * c
page = (k - 1) // per_page + 1
pos = (k - 1) % per_page + 1
col = (pos - 1) // n + 1
row = (pos - 1) % n + 1

print('страница', page, 'столбец', col, 'строка', row)