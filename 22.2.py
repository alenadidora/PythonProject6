n = int(input())
k = int(input())
m = int(input())

trips = n * 2

sessions = trips // k + (1 if trips % k != 0 else 0)

print(sessions * m)