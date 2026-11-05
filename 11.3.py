
best_score = int(input())

score = int(input())

while score != -1:
    if score > best_score:
        best_score = score

    score = int(input())

print(best_score)



