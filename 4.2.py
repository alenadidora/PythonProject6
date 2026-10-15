score = input()

team1, team2 = map(int, score.split(':'))


if team1 > team2:
    print(1)
elif team1 < team2:
    print(2)
else:
    print(0)