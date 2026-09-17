X, Y = map(int, input().split())
print(1 if (Y and X % Y == 0) or (X and Y % X == 0) else 0)