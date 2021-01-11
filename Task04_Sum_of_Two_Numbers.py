start = int(input())
end = int(input())
magic_number = int(input())
combination = 0
is_combination = False

for i in range(start, end+1):
    if is_combination:
        break
    for j in range(start, end+1):
        combination += 1
        if i + j == magic_number:
            print(f"Combination N:{combination} ({i} + {j} = {magic_number})")
            is_combination = True
            break

if not is_combination:
    print(f"{combination} combinations - neither equals {magic_number}")



