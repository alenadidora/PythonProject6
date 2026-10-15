n = int(input())

if n == 1:
    print(0)
else:
    n -= 1

    if n <= 9:
        print(n)

    else:
        n -= 9
        full = n // 2
        digit = n % 2
        number = 10 + full

        if digit == 0:
            result = number // 10
        else:
            result = number % 10

        print(result)