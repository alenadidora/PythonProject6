
n = int(input())

last = n % 10
two = n % 100

if last == 1 and two != 11:
    print(n, "попугай")
elif 2 <= last <= 4 and not(12 <= two <= 14):
    print(n, "попугая")
else:
    print(n, "попугаев")