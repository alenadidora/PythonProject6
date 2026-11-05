numbers = []
for i in range(100, 1000):
    if i % 17 == 0:
        numbers.append(str(i))

print(" ".join(numbers))
print(len(numbers))