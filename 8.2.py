print("Здравствуйте! Как Вас зовут?", end=" ")
name = input()

print(f"Очень приятно, {name}! Меня зовут Марк.")

print("Сколько Вам лет?", end=" ")
age = int(input())


mark_age = 81

difference = mark_age - age

if difference > 0:
    print(f"Да, {name}, я старше Вас на {difference} лет.")
elif difference < 0:
    print(f"Да, {name}, Вы старше меня на {difference} лет.")
else:
    print(f"Да, {name}, мы с Вами ровесники!")

print("Вам нравится программировать?", end=" ")
answer = input()

if answer == "да":
    print("Превосходно! Уверен, у Вас получится написать множество полезных и хороших программ.")
else:
    print("Жаль. Я думал, Вы сможете написать интересную программу для меня.")