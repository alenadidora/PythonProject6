x = int(input())
count = 0

for a in range(1, int(x ** 0.5) + 1):
    rem = x - a ** 2 
    b = int(rem ** 0.5)

    if b ** 2 == rem and b >= a:
        count += 1

print(count)
