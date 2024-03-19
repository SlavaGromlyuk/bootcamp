# This is a LOTTO game

def lotto(prize):
    
    import random

    count = 1
    matching_nums = 0
    matching_nums_list = []
    prize = 0
    selected_nums = []

    while True:
        choice = input("Enter 1 to pick your numbers or 2 to play a lucky dip: ")
        if choice == "1":
            while len(selected_nums) < 6:
                num = int(input(f"Enter number {count}: "))
                if 0 < num < 60:
                    selected_nums.append(num)
                else:
                    print("Please pick the numbers between 1 and 59.") 
                    continue
                count += 1
            break
        elif choice == "2":
            selected_nums = random.sample(range(1,49), 6)
            break
        else: 
            print("Your entry was not recognised. Please try again.")
            continue 
                    
    selected_nums.sort()
    
    print(f"You picked the followig numbers: {selected_nums}.")

    random_nums = random.sample(range(1,49), 6)
    
    random_nums.sort()
    
    print(f"The winning numbers are: {random_nums}.")

    for i in selected_nums:
        if i in random_nums:
            matching_nums += 1
            matching_nums_list.append(i)
        i += 1

    if matching_nums == 6:
        print(f"Congratulations! Your have 6 matching numbers: {matching_nums_list}. You won $1,000,000!")
        prize = 1000000

    elif matching_nums == 5:
        print(f"Congratulations! Your have 5 matching numbers: {matching_nums_list}. You won $175,000.")
        prize = 175000
        
    elif matching_nums == 4:
        print(f"Congratulations! Your have 4 matching numbers: {matching_nums_list}. You won $1,400.")
        prize = 1400
        
    elif matching_nums == 3:
        print(f"Congratulations! Your have 3 matching numbers: {matching_nums_list}. You won $300.")
        prize = 300
        
    elif matching_nums == 2:
        print(f"Congratulations! Your have 2 matching numbers: {matching_nums_list}. You won $20")
        prize = 20
         
    elif matching_nums == 1:
        print(f"Your have 1 matching number: {matching_nums_list}. You won $1.")
        prize = 1
    
    else:
        print(f"Unfortunately you do not have any matching numbers.")

    return prize

print('''
Welcome to LOTTO sim game.
Try your luck in guessing six random numbers (between 1 and 59) to win a prize!
''')

total = 10

while True:
    print(f"You have ${total}. Each game costs $2.\n") 
    if total <= 1:
        print(f"I am sorry you do not have enough money to play. Your balance is ${total}. Good bye!")
        exit()
    selection = input("Do you want play (y/n)? ").lower()
    if selection.startswith("y") == True:
        total = total - 2
        total = total + lotto(total)
    else:
        print(f"Thank you for playing. Your balance is ${total}.")
        exit()