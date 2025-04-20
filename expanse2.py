# Expense Tracker - Default keeps adding expenses until option 2 or 3 is chosen

def main():
    expenses = []

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense (Default)")
        print("2. Show Summary")
        print("3. Exit")
        
        choice = input("Choose an option (press Enter to add expense): ").strip()

        # Default: Add Expense
        if choice == '' or choice == '1' :
            name = input("Enter expense name: ")
            try:
                amount = float(input("Enter amount: "))
                expenses.append((name, amount))
                print(f"Added: {name} - ₹{amount}")
            except ValueError:
                print("Invalid amount! Please enter a number.")

        elif choice == '2':
            if not expenses:
                print("No expenses recorded.")
                continue
            total = sum(amount for _, amount in expenses)
            print("\n--- Expense Summary ---")
            for i, (name, amount) in enumerate(expenses, start=1):
                print(f"{i}. {name} - ₹{amount}")
            print(f"\nTotal Expenses: ₹{total}")

        elif choice == '3':
            print("Exiting Expense Tracker.")
            break

        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()
