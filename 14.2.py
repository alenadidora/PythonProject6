
N = int(input())


galleons = N // (17 * 29)
knuts1 = N % (17 * 29)

sickles = knuts1 // 29
knuts = knuts1 % 29

if galleons > 0:
    print(galleons, 'галлеона', end=' ')
if sickles > 0:
    print(sickles, 'сикля', end=' ')
if knuts > 0:
    print(knuts, 'кната')