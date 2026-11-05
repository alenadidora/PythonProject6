temp = float(input())
count = 0

while temp != 0:
    prev_temp = temp
    temp = float(input())

    if temp != 0 and temp < prev_temp:
        count += 1

print(count)



