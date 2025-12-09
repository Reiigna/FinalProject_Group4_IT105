# ==============================
# STUDENT DAILY EXPENSE TRACKER
# Covers: variables, input, lists, loops, conditional statements, functions
# ==============================

def show_expense_menu():
    print("\nChoose your expense category:")
    print("1. Food & Meals 🍽️") # Breakfast, Lunch, Dinner
    print("2. Battle of the Bus/Jeep/Tricycle 🚌") # Commute to School
    print("3. Budol Booth Treasures 🎁") # Other School Stuff
    print("4. Bilhan na kita snacks, babe 🍪") # Snacks
    print("5. Post-School Adventures 🛍️") # Mall / Other Places
    print("6. Journey Back Home 🏠") # Commute Home
    print("7. Done for Today ✨") # Finish

def show_food_menu():
    print("\nChoose what meal of the day:")
    print("A. Breakfast ka na, Love 🥞") # Breakfast
    print("B. Eat ka Launch, Baby 🍱") # Lunch
    print("C. Dinner na tayo, Mahal 🍲") # Dinner
    print("D. Date with my forever 💖") # Date 

def handle_food_choice():
    while True:
        show_food_menu()
        choice = input("Enter your food choice (A-D): ").upper()

        if choice == "A":
            add_expense("Food: Breakfast 🥞")
            break
        elif choice == "B":
            add_expense("Food: Lunch 🍱")
            break
        elif choice == "C":
            add_expense("Food: Dinner 🍲")
            break
        elif choice == "D":
            date_name = input("Who did you go on a date with? (e.g., Liv): ")
            add_expense(f"Food: Date with {date_name} 💖")
            break
        else:
            print("Invalid choice. Please select from A-C.")

def add_expense(category_name):
    while True:
        try:
            amount = float(input(f"Enter amount spent for {category_name}: ₱"))
            if amount < 0:
                print("Amount cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a numeric value.")
    expenses.append((category_name, amount))
    print(f"Added: {category_name} - ₱{amount:.2f}")


def view_expenses():
    if not expenses:
        print("\nNo expenses recorded yet.\n")
        return
    print("\n--- TODAY'S EXPENSES ---")
    for i, (cat, amt) in enumerate(expenses, 1):
        print(f"{i}. {cat} | ₱{amt:.2f}")


def calculate_total():
    total = sum(amount for _, amount in expenses)
    return total


def budget_summary():
    total = calculate_total()
    spending_allowance = allowance - savings_goal  # reserved savings
    remaining_spending = spending_allowance - total

    if remaining_spending >= 0:
        print(f"\nTotal Spent Today: ₱{total:.2f}")
        print(f"Remaining Allowance for spending (after reserving savings): ₱{remaining_spending:.2f}")
        print("You are within your spending allowance. Savings remain untouched. 💰")
        remaining_savings = savings_goal
    else:
        # overspending: deduct from savings
        overspend = abs(remaining_spending)
        remaining_savings = savings_goal - overspend
        print(f"\nTotal Spent Today: ₱{total:.2f}")
        print(f"You spent beyond your daily allowance by ₱{overspend:.2f}!")
        if remaining_savings > 0:
            print(f"Remaining Savings Goal: ₱{remaining_savings:.2f}")
        else:
            remaining_savings = 0
            print("⚠ Warning: You've used up all your savings for your goal item!")

    # Summary of savings progress
    if remaining_savings >= savings_goal:
        print(f"💰 Progress: Your savings goal for {goal_item} is safe!")
    elif remaining_savings > 0:
        print(f"💰 Partial savings remaining: ₱{remaining_savings:.2f} for your goal item {goal_item}")
    else:
        print(f"💰 No savings left for your goal item {goal_item}. Be careful next time!")



def main():
    print("===== STUDENT DAILY EXPENSE TRACKER =====\n")

    # 1. Student Info
    name = input("Enter your name: ")
    year = input("Enter your college year (e.g. 1st Year): ")
    start_time = input("Enter your school start time (ex. 7:30 AM): ")
    end_time = input("Enter your school end time (ex. 4:30 PM): ")

    # 2. Allowance & Savings
    global allowance
    while True:
        try:
            allowance = float(input("Enter your weekly or monthly allowance: ₱"))
            if allowance < 0:
                print("Allowance cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a numeric value.")

    global savings_goal
    while True:
        try:
            savings_goal = float(input("Enter how much you want to save: ₱"))
            if savings_goal < 0 or savings_goal > allowance:
                print("Savings goal cannot be negative or exceed your allowance. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a numeric value.")

    global goal_item
    goal_item = input("Enter the item you have been wanting to buy: ")

    print(f"\nHello {name} ({year})! Let's track your expenses today from {start_time} to {end_time} and work towards buying {goal_item}.\n")

    # List to store expenses
    global expenses
    expenses = []

    # Main expense entry loop
    while True:
        show_expense_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            handle_food_choice()
        elif choice == "2":
            add_expense("Battle of the Bus/Jeep 🚌")
        elif choice == "3":
            item_name = input("What school-related item did you buy? ")
            add_expense(f"Budol Booth Treasures 🎁 - {item_name}")
        elif choice == "4":
            add_expense("Bilhan na kita snacks, babe 🍪")
        elif choice == "5":
            place_name = input("Where did you go after school? ")
            add_expense(f"Post-School Adventures 🛍️ - {place_name}")
        elif choice == "6":
            add_expense("Journey Back Home 🏠")
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please select from 1-8.")

    # Show final report
    print("\n===== DAILY EXPENSE SUMMARY =====")
    print(f"Student Name: {name}")
    print(f"College Year: {year}")
    print(f"School Time: {start_time} - {end_time}\n")
    view_expenses()
    budget_summary()
    print("\nThanks for using the Student Daily Expense Tracker! Keep saving and budgeting wisely.")


# Run the program
main()
