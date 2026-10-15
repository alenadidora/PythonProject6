n = int(input())

if 1000 <= abs(n) <= 9999:
    n = abs(n)
    if n // 1000 == n % 10 and (n // 100) % 10 == (n // 10) % 10:
        print("Настоящее")
    else:
        print("Кривое")
else:
    print("Число не четырехзначное")