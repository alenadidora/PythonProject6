
x = input()
y = int(input())

x_num = ord(x) - 96

sum = x_num + y

if sum % 2 == 0:
    print('белый')
else:
    print('чёрный')