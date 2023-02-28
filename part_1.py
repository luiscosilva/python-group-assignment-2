''' **************************************************************************
Course: Object-Oriented Programming 1
Assignment: Programming Strategies
Authors (Group 01):
    - Chris Johnson
    - Samreet Kaur
    - Luis Silva

Date: FEV-19-2023

=> Part #01
************************************************************************** '''

# The profit_table variable is a dictionary that holds the profit for each product category
profit_table = {1: 120.45, 2: 99.50, 3: 75.69, 4: 65.73, 5: 51.49}

# The prod_list variable is a dictionary that holds the quantity for each product category (initialized by zero)
prod_list = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

# The total_profit variable will be used to store the final profit amount
total_profit = 0

# The variable keep_entering_products is a flag that controls whether the loop will continue or not
keep_entering_products = True

print("Welcome to Circle Phones' Profit calculator.\n")

# This loop is used to collect the product categories and their quantities
while(keep_entering_products):

    prod_category = int(input("Enter product number 1-5, or enter 0 to stop:\n\t"))

    # Validation for invalid category input
    if(prod_category < 0 or prod_category > 5):
        print("Invalid input, please enter a valid number\n")
    else:
        if(prod_category == 0):
            # breaks the loop
            keep_entering_products = False
        else:
            prod_qty = int(input("Enter quantity sold:\n\t"))
            prod_list[prod_category] += prod_qty

# This loop gets each category number and quantity from prod_list and multiplies for the respective profit amount
for key, value in prod_list.items():
    total_profit += (profit_table[key] * value)

# Display the total profit
print(f"Your total profit for today is: {total_profit}")