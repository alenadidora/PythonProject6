
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())


side_1 = min(c, d, e)
if c == side_1:
    side_2 = min(d, e)
elif d == side_1:
    side_2 = min(c, e)
else:
    side_2 = min(c, d)

if (side_1 <= a and side_2 <= b) or (side_1 <= b and side_2 <= a):
    print("да")
else:
    print("нет")