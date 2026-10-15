import math

r = float(input())
a = float(input())
b = float(input()) 

arena_area = math.pi * r * r
carpet_area = a * b

if carpet_area <= arena_area:
    print('да')
else:
    print('нет')