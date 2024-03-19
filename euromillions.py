# This is a EUROMILLIONS game

def pick_nums (a, b):
    
    import random

    selected_nums = []
    count = 1
       
    while True:
        choice = input("Enter 1 to pick your numbers or 2 to play a lucky dip: ")
        if choice == "1":
            while len(selected_nums) < b:
                num = int(input(f"Enter number {count}: "))
                if num in selected_nums:
                    print("This number is already in your list. Pick another one")
                    continue
                else:
                    if 0 < num <= a:
                        selected_nums.append(num)
                    else:
                        print(f"Please pick the number between 1 and {a}.") 
                        continue
                count += 1
            break
        elif choice == "2":
            selected_nums = random.sample(range(1,a), b)
            break
        else: 
            print("Your entry was not recognised. Please try again.")
            continue 
                    
    selected_nums.sort()
    
    return selected_nums

def match_nums(selected_nums, random_nums):

    matching_nums_list = []

    for i in selected_nums:
        if i in random_nums:
            matching_nums_list.append(i)
        i += 1

    return matching_nums_list

def check_prize(matching_nums_list, matching_lucky_stars, prize_fund):
    
    prize = 0

    winning_comb = len(matching_nums_list) + len(matching_lucky_stars)/10

    if winning_comb in prize_fund.keys():
        print(f"Congratulations! You won ${prize_fund.get(winning_comb)}!")
        prize = prize_fund.get(winning_comb)
 
    else:
        print(f"Unfortunately you did not win any prize.")

    return prize

def euromillions():
    
    import random

    print ("Select five main numbers (between 1 and 50)") 
    selected_nums = pick_nums(50, 5)

    print ("Now select two Lucky Star numbers (between 1 and 12)") 
    lucky_stars = pick_nums(12,2)

    print(f"You picked the followig numbers: {selected_nums} and two Lucky Stars numbers {lucky_stars}.")

    random_nums = random.sample(range(1,50), 5)

    random_lucky_stars = random.sample(range(1,12), 2)
    
    random_nums.sort()

    random_lucky_stars.sort()
    
    print(f"The winning main numbers are {random_nums} and two Lucky Stars numbers are {random_lucky_stars}.")

    matching_nums_list = match_nums(selected_nums, random_nums)

    matching_lucky_stars = match_nums(lucky_stars, random_lucky_stars)

    print(f"Your have {len(matching_nums_list)} matching main numbers {matching_nums_list} and \
{len(matching_lucky_stars)} matching Lucky Stars numbers {matching_lucky_stars}.")
    
    prize_fund = {
    1 : 1,
    1.1 : 1.50,
    1.2 : 4.30,
    2 : 2.50,
    2.1 : 3.60,
    2.2 : 9.10,
    3 : 6,
    3.1 : 7.30,
    3.2 : 37.30,
    4 : 25.60,
    4.1 : 77.80,
    4.2 : 844.70,
    5 : 13561.20,
    5.1 : 130554.30,
    5.2 : 1000000
    }    

    return check_prize(matching_nums_list, matching_lucky_stars, prize_fund)

print('''
Welcome to EUROMILLIONS sim game.
Try your luck in guessing five random numbers (between 1 and 50) and two Lucky Star numbers (between 1 and 12) to win a prize!
''')

total = 10

while True:
    print(f"You have ${total}. Each game costs $2.50.\n") 
    if total < 2.50:
        print(f"I am sorry you do not have enough money to play. Your balance is ${total}. Good bye!")
        exit()
    selection = input("Do you want play (y/n)? ").lower()
    if selection.startswith("y") == True:
        total = total - 2.50
        total = total + euromillions()
    else:
        print(f"Thank you for playing. Your balance is ${total}.")
        exit()