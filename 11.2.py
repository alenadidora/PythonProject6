import turtle as t
import math

xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())


t.penup()
t.goto(xc, yc-r) # Перемещаемся к нижней точке круга
t.pendown()
t.circle(r)


distance = math.sqrt((x - xc)**2 + (y - yc)**2)
if distance == r:
    print("Точка на окружности")
elif distance < r:
    print("Точка внутри окружности")
else:
    print("Точка вне окружности")