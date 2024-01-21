import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
        date = datetime.date.today()
        expense = {'Date': date, 'Amount': amount, 'Category': category}
        self.expenses.append(expense)
        print("Expense added successfully.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses to display.")
            return

        print("\nExpense Summary:")
        for expense in self.expenses:
            print(f"Date: {expense['Date']} | Amount: {expense['Amount']} | Category: {expense['Category']}")

    def view_spending_patterns(self):
        if not self.expenses:
            print("No expenses to analyze.")
            return

        categories = {}
        for expense in self.expenses:
            category = expense['Category']
            categories[category] = categories.get(category, 0) + expense['Amount']

        print("\nSpending Patterns:")
        for category, total_amount in categories.items():
            print(f"{category}: {total_amount}")

if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Spending Patterns")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter the expense amount: "))
            category = input("Enter the expense category: ")
            tracker.add_expense(amount, category)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.view_spending_patterns()
        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
