next_movie = input()
standard_tickets = 0
student_tickets = 0
kids_tickets = 0

while next_movie != "Finish":
    capacity = int(input())
    tickets = 0
    while tickets < capacity:
        next_ticket = input()
        if next_ticket == "End":
            break
        tickets += 1
        if next_ticket == "standard":
            standard_tickets += 1
        elif next_ticket == "student":
            student_tickets += 1
        else:
            kids_tickets += 1

    print(f"{next_movie} - {(tickets / capacity) * 100:.2f}% full.")
    next_movie = input()

total_tickets = standard_tickets + student_tickets + kids_tickets
print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard_tickets / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kids_tickets / total_tickets) * 100:.2f}% kids tickets.")
