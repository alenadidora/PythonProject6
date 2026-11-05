n = int(input())
questions = 0
max_range = 1

while max_range < n:
    max_range = max_range * 2
    questions += 1

print(questions)

