att = float(input())
comp = float(input())
yds = float(input())
td = float(input())
int_ = float(input())

a = (att - 1) / att * 100 if att > 0 else 0
b = comp / att * 100 if att > 0 else 0
c = yds / att * 100 if att > 0 else 0
d = td / att * 100 if att > 0 else 0
e = 2.375 - (int_ / att * 100) if att > 0 else 0

a = min(max(a, 0), 2.375)
b = min(max(b, 0), 2.375)
c = min(max(c, 0), 2.375)
d = min(max(d, 0), 2.375)
e = min(max(e, 0), 2.375)

rating = (a + b + c + d + e) / 6 * 100

print(rating)