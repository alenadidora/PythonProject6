
X, Y, N = map(int, input().split())
price_kop = X * 100 + Y
total_kop = price_kop * N
rubles = total_kop // 100
kop = total_kop % 100
print(rubles, 'руб.', kop, 'коп.')