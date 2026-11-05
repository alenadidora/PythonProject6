num = int(input())

while int(num ** 0.5) ** 2 != num:
    num = int(input("Это не полный квадрат. Введите другое число: "))

print("Это полный квадрат!")