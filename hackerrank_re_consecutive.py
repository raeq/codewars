import re


s = "HackerRank"

expr = r'([a-zA-Z0-9])\1'
m = list(re.finditer(expr, s))

if m:
    for matchNum, match in enumerate(m, start = 1):
        print(match.group()[1])
        break
else:
    print(-1)
