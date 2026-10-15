
N = int(input())
K = int(input())
M = int(input())

s1 = abs(K - M)

s2 = N - s1

print(min(s1, s2))