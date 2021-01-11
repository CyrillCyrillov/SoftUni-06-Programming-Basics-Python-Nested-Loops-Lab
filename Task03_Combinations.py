n = int(input())
combination_number = 0

for i in range(0, n+1):
    for j in range(0, n+1):
        for x in range(0, n+1):
            if x + j + i == n:
                combination_number += 1
print(combination_number)