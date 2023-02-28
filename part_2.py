''' **************************************************************************
Course: Object-Oriented Programming 1
Assignment: Programming Strategies
Authors (Group 01):
    - Chris Johnson
    - Samreet Kaur
    - Luis Silva

Date: FEV-20-2023

=> Part #02
************************************************************************** '''

# The profit_table variable is a dictionary that holds the profit for each product category
profit_table = {1: 120.45, 2: 99.50, 3: 75.69, 4: 65.73, 5: 51.49}

# The prod_list variable is a dictionary that holds the quantity for each product category (initialized by zero)
prod_list = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

# The period_days variable is a dictionary that holds the days of week for every period
period_days = {
    1: [""],
    2: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    3: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    4: ["Saturday", "Sunday"]
}

# The period_name variable is a dictionary that holds the name of the periods
period_name = {
    1: "",
    2: "the week",
    3: "the week (business days)",
    4: "the weekend"
}

# The total_profit variable will be used to store the final profit amount
total_profit = 0

# The keep_running variable is a flag that will keep the program working
keep_running = True

# The variable keep_entering_products is a flag that controls whether the loop will continue asking for products or not
keep_entering_products = True

print("\nWelcome to Circle Phones' Profit calculator.")


while(keep_running):

    print("You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend\n")
    print("Enter:")
    print("1 - For specific Day")
    print("2 - For the Week")
    print("3 - For Week Business Days")
    print("4 - For Weekend days")
    print("0 - Exit\n")

    period = int(input())

    if(period == 0):
        keep_running = False
    else:
        if(period == 1):
            valid_day = False
            
            while not(valid_day):
                selected_day = input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]:\n")

                #Format the day of the week with the first character uppercase and the rest lowercase
                formatted_selected_day = selected_day[0].upper() + selected_day[1:len(selected_day)].lower()

                # Check whether the day of the week entered is valid
                if(formatted_selected_day in period_days[2]):
                    valid_day = True
                    period_days[period][0] = formatted_selected_day
                    period_name[period] = formatted_selected_day
                else:
                    print("Error: Invalid day.\n")

        for day in period_days[period]:

            print(f"For {day}\n")

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

        total_profit = round(total_profit, 2)

        # Display the total profit
        print(f"\nYour total profit for {period_name[period]} is: ${total_profit}")

        # Final message
        if(total_profit >= 10000.00):
            print("You did well this period! Keep up the great work!\n")
        else:
            print("We didn't reach our goal for this period. More work is needed.\n")