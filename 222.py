x, y = map(int, input().split())
print(1 if (y and x % y == 0) or (x and y % x == 0) else 0)