# Provide an explanation to the user of the purpose of the prograwme and the choice he/she needs to make

import math

print('''
This programme calculates the return on investment using simple and compound interest. 
It also calculates the monthly repayment amount for the bond.

investment - to calculate the amount of interest you'll earn on your investment\n
bond       - to calculate the amount you'll have to pay on a home loan
''')

# Prompt user to make the choice and store it in a variable. Convert the value of a variable to lower case.

choice = input("Enter either 'investment' or 'bond' from the menue above to proceed: ").lower()

# Check if choice option typed by user is valid and print confirmation or error message

if choice == "investment":
    print("To calculate the return on investment I need the following data from you.")
elif choice == "bond":
    print("To calculate the repayment on the bond I need the following data from you.") 
else:
    print("Sorry, I have not recognised your choice")

# Statement block for investment

# Get values from user for variables (domain) 

if choice == "investment":
    deposit = float(input("Please enter the amount of money you are depositing: "))
    rate = float(input("Please enter the interest rate: "))
    term = int(input("How many years you plan on investing? "))
    interest = input("Do you want simple or compound interest? ").lower()

# Perform calculation of a total return (range) based on both types of interest

    total_simple = round(deposit * (1 + (rate/100) * term), 2)
    total_compound = round(deposit * math.pow((1 + (rate/100)),term), 2)

# Print relevant total (range) depending on the type of interest chosen by the user

    if interest == "simple":
        print(f"At the end of a term you will get a total of {total_simple}")
    else:
        print(f"At the end of a term you will get a total of {total_compound}")

# Statement block for bonds

# Get values from user for variables (domain) 

if choice == "bond":
    house_value = float(input("What is the present value of the house?: "))
    rate = float(input("Please enter the interest rate: "))
    term = int(input("How many months you plan to take to repay the bond? "))

# Perform calculation of a total repayment

    repayment = round(((rate/100/12) * house_value) / (1 - (1 + (rate/100/12)) ** (- term)), 2)

# Print the monthly repayment figure

    print(f"Each month you will have to repay {repayment}")