floors = int(input())
rooms = int(input())

for i in range(floors, 0, -1):
    if i == floors:
        type = "L"
    elif i % 2 == 0:
        type = "O"
    else:
        type = "A"
    for x in range(0, rooms):
        print(f"{type}{i}{x}", end=" ")

    print()
