raw = input('Enter number: ')
try:
    num = int(raw)
    print(num)
except ValueError:
    print('Ошибка: введено не число')




raw = input('Enter number:')
if raw.isdigit():
    print(int(raw))
else:
    print("Вы ввели не число!")