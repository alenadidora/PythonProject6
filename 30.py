att = int(input("Введите количество попыток: "))
comp = int(input("Точные пасы: "))
yds = int(input("Ярды: "))
td = int(input("Тачдауны: "))
int_ = int(input("Перехваты: "))

a = ((comp / att) - 0.3) * 5 
b = ((yds / att) - 3) * 0.25
c = (td / att) * 20
d = 2.375 - ((int_ / att) * 25)

a = max(0, min(a, 2.375))
b = max(0, min(b, 2.375))
c = max(0, min(c, 2.375))
d = max(0, min(d, 2.375))

rating = ((a + b + c + d) / 6) * 100
print(rating)

