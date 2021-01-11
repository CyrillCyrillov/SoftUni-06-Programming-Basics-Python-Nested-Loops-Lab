city = " "
saved_money = 0
needed_money = 0

while city != "End":
    city = input()
    if city != "End":
        needed_money = float(input())
        while saved_money < needed_money:
            next_money = float(input())
            saved_money += next_money


    if city != "End":
        print(f"Going to {city}!")
    # saved_money -= needed_money
    saved_money = 0