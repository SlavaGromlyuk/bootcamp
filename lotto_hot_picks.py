# This is a LOTTO game

def lottohotpicks(prize):
    
    import random

    count = 1
    matching_nums = 0
    matching_nums_list = []
    prize = 0
    selected_nums = []

    num_list = int(input("How many numbers you want to play (1 to 5)? : "))

    while True:
        choice = input("Enter 1 to pick your numbers or 2 to play a lucky dip: ")
        if choice == "1":
            while len(selected_nums) < num_list:
                num = int(input(f"Enter number {count}: "))
                if 0 < num < 60:
                    selected_nums.append(num)
                else:
                    print("Please pick the numbers between 1 and 59.") 
                    continue
                count += 1
            break
        elif choice == "2":
            selected_nums = random.sample(range(1,49), num_list)
            break
        else: 
            print("Your entry was not recognised. Please try again.")
            continue 
                    
    selected_nums.sort()
    
    print(f"You picked the followig numbers: {selected_nums}.")

    random_nums = random.sample(range(1,49), num_list)
    
    random_nums.sort()
    
    print(f"The winning numbers are: {random_nums}.")

    for i in selected_nums:
        if i in random_nums:
            matching_nums += 1
            matching_nums_list.append(i)
        i += 1

    if matching_nums == 5:
        print(f"Congratulations! Your have 5 matching numbers: {matching_nums_list}. You won $350,000!")
        prize = 350000

    elif matching_nums == 4:
        print(f"Congratulations! Your have 4 matching numbers: {matching_nums_list}. You won $13,000.")
        prize = 13000
        
    elif matching_nums == 3:
        print(f"Congratulations! Your have 3 matching numbers: {matching_nums_list}. You won $800.")
        prize = 800
        
    elif matching_nums == 2:
        print(f"Congratulations! Your have 2 matching numbers: {matching_nums_list}. You won $60.")
        prize = 60
       
    elif matching_nums == 1:
        print(f"Your have 1 matching number: {matching_nums_list}. You won $6.")
        prize = 6
    
    else:
        print(f"Unfortunately the numbers you picked do not match the winning numbers.")

    return prize

print('''
Welcome to LOTTO HOT PICKS sim game.
Try your luck in picking and matching random numbers (between 1 and 59) to win a prize!
''')

total = 10

while True:
    print(f"You have ${total}. Each game costs $1.\n") 
    if total == 0:
        print(f"I am sorry you do not have enough money to play. Your balance is ${total}. Good bye!")
        exit()
    selection = input("Do you want play (y/n)? ").lower()
    if selection.startswith("y") == True:
        total = total - 1
        total = total + lottohotpicks(total)
    else:
        print(f"Thank you for playing. Your balance is ${total}.")
        exit()