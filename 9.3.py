n, k, r = map(float, input().split())

day = 1
length = n

while length < r:
    length = length + (length * k / 100)
    day += 1

print(day)


