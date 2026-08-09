"""CLI Expense Tracker"""

import logging
 
from expense_tracker import ExpenseTracker
 
logging.basicConfig(
    filename="expense_tracker.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


MENU = """
==== Expense Tracker ====
1. Add expense
2. View all expenses
3. View expenses by category
4. Delete expense
5. View total spending
6. View spending by category
7. Exit
"""

def main():
    tracker = ExpenseTracker()
    print("Welcome to Expense Tracker")

    while True:
        print(MENU)
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_expense(tracker)
        elif choice == "2":
            print_expenses(tracker.list_expenses())
        elif choice == "3":
            category = input("Enter category: ").strip()
            print_expenses(tracker.list_expenses(category))
        elif choice == "4":
            delete_expense(tracker)
        elif choice == "5":
            print(f"\nTotal spending: ${tracker.total_spending():,.2f}")
        elif choice == "6":
            print_summary(tracker.spending_by_category())
        elif choice == "7":
            print("GoodBye!")
            break
        else:
            logging.warning("User entered invalid menu option: %r", choice)
            print("Invalid option. Please choose a number between 1 and 7.")    

def add_expense(tracker):
    category = input("Category: (eg: Food, Rent, Transport): ").strip()
    description = input("Description: ").strip()

    if not category or not description:
        print("Category and Description cannot be empty!")
        return

    try:
        amount = float(input("Amount ($): ").strip())
    except ValueError:
        print("Please enter a valid amount")
        return

    try:
        expense = tracker.add_expense(category, description, amount)
    except ValueError as error:
        print(error)
        return

    print(expense)


def delete_expense(tracker):
    raw_id = input("Enter the ID of the expense to delete: ").strip()
    try:
        expense_id = int(raw_id)
    except ValueError:
        print("Please enter a valid numeric ID.")
        return
 
    if tracker.delete_expense(expense_id):
        print(f"Expense {expense_id} deleted.")
    else:
        print(f"No expense found with ID {expense_id}.")


def print_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return
 
    print()
    for expense in expenses:
        print(expense)

def print_summary(summary):
    if not summary:
        print("\nNo expenses recorded yet.")
        return
 
    print("\n--- Spending by Category ---")
    for category, amount in sorted(summary.items(), key=lambda item: item[1], reverse=True):
        print(f"{category:<15} ${amount:,.2f}")

if __name__ == "__main__":
    main()