pin = int(input())

if pin % 2 != 0:
    print("ERROR")
else:
    a = pin // 1000
    b = (pin // 100) % 10
    c = (pin // 10) % 10
    d = pin % 10
    if a == b or b == c or c == d:
        print("ERROR")
    else:
        if 1900 <= pin <= 2050:
            print("ERROR")
        else:
            print("OK")