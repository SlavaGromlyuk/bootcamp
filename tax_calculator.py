# This programme calculates your income tax liability

# Below is a set of fixed parameters for 2023-2024 financial year

br = 0.2 # basic tax rate
hr = 0.4 # higher tax rate
ar = 0.45 # additional tax rate
brt = 37700 # basic rate threshold
hrt = 125140 # higher rate threshold
pa = 12570 # personal allowance
pat = 100000 # personal allowance threshold
nilt = 242*52 # national insurance lower threshold (annually)
niht = 967*52 # national insurance higher threshold (annually)
nilr = 0.12 # national insurance lower rate
nihr = 0.02 # national insurance higher rate

# Below are the prompts for user to set the value of variable parameters

gross_income = int(input("What is your gross annual income ? : "))

# Below is calculation of personal allowance

if hrt > gross_income >= pat:
    pa = pa - (gross_income - pat)/2
    
elif gross_income >= hrt:
    pa = 0
    
taxable_income = gross_income - pa

# Below is calculation of income tax liability

if taxable_income <= brt:
    tax = taxable_income * br

elif taxable_income <= hrt:
    tax = brt * br + (taxable_income - brt) * ar

elif taxable_income > hrt:
    tax = brt * br + (hrt - brt) * hr + (taxable_income - hrt) * ar

# Below is calculation of national insurance contributions

if gross_income < nilt:
    ni = 0
elif nilt <= gross_income <= niht:
    ni = (gross_income - nilt) * nilr
elif gross_income >= niht:
    ni = (gross_income - nilt) * nilr + (gross_income - nilt - niht) * nihr

# Below is calculation of the the net income

net_income = round(gross_income - tax - ni, 2)

# Output to user the results of calculations

print(f'''
Your tax free personal allowance is {round(pa, 2)}
Your annual taxable income is {round(taxable_income, 2)}
Your annual income tax liability is {round(tax, 2)}
Your annual NI liability is {round(ni, 2)}
Your annual net income is {round(net_income, 2)}
Your monthly net income is {round(net_income/12, 2)}
''')