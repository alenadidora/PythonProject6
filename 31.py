x, y = map(int, input().split())
print((x != 0 and y % x == 0) or (y != 0 and x % y == 0))
