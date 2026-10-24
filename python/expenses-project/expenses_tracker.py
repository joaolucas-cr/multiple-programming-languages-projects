"""
24/10/2026
Time:

"""

from storage import Storage
from expense import Expense
from datetime import date as dateClass
from sys import exit
from time import sleep

def main():

    print("\n\nEXPENSE TRACKER\n")

    storage = Storage()
    exps = storage.getExpense()
    expenses = []
    for exp in exps:
        expenses.append(Expense(exp['amount'], exp['category'], exp['description'], exp['date'], id=exp['id']))
    budget = storage.getBudget()
    running = True
    while(running):
        if(budget > 0):
            remaining = budget - sum(expense.amount for expense in expenses if expense.date.month == dateClass.today().month)
            print(f"\n Budget: {budget:.2f} | Remaining: {remaining:.2f} \n")
            if(remaining < 0):
                print("WARNING: your total expenses are greater than your budget")

        print("Which action do you want to take?")
        actions = ["Add Expense", "View Expenses", "Edit Expense", "Delete Expanse", "Summary", "Set Budget"]
        for i, _ in enumerate(actions):
            print(f"{i+1}: {actions[i]}")
        print("\nPress a valid key (if you want to quit type exit):")
        action = input()

        if(action == "exit"):
            exit()

        try:
            action = int(action)
        except:
            print("Invalid key!\n")
            continue
        print()

        match action:
            case 1:
                print("Amount?")
                amount = input()

                print(f"\nCategories: {', '.join(Expense.categories)}")
                category = input()

                print("\nDescription?")
                description = input()

                print("\nDate: format (YYYY-MM-DD)")
                date = input()

                try:
                    expense = Expense(float(amount), category, description, date)
                    expenses.append(expense)
                    storage.saveExpenses(expenses)
                    print("\nSucessfully created the expense!")
                    print(expense, '\n')
                except Exception as error: 
                    print(f"ERROR: {error}")

            case 2:
                if(len(expenses) == 0):
                    print("No expenses registered.")
                    pass
                for expense in expenses:
                    print(expense)

            case 3:
                print("ID of the expense:")
                expense_id = input()
                found = False
                for expense in expenses:
                    if expense.getID() == expense_id:
                        
                        found = True
                        print("Amount?")
                        amount = input()

                        print(f"\nCategories: {', '.join(Expense.categories)}")
                        category = input()

                        print("\nDescription?")
                        description = input()

                        print("\nDate: format (YYYY-MM-DD)")
                        date = input()

                        expense.update(amount, description, category, date)
                        storage.saveExpenses(expenses)

                if(not found):
                    print("\nNo record found")

            case 4: 
                print("ID of the expense to delete")
                expense_id = input()
                found = False
                for i, expense in enumerate(expenses):
                    if expense.getID() == expense_id:
                        print("Are you sure about it? Type: yes")
                        answer = input()
                        if(answer == "yes"):
                            expenses.pop(i)
                            found = True
                            storage.saveExpenses(expenses)

                            print("\n Successfully deleted expense.")
                        else:
                            print("Operation cancelled")
                if not found:
                    print('Expense not found')

            case 5:
                totalExpense = sum(expense.amount for expense in expenses)
                print("Total expense:", totalExpense)
                for category in Expense.categories:
                    print(f"{category}: {sum(expense.amount for expense in expenses if expense.category == category)}")
                
                runningSummary = True
                while(runningSummary):
                    print("\nType the month number to filter per month or \"quit\" in order to get back to the main screen. (January: 1, February: 2, etc...)")
                    inp = input()

                    for expense in expenses:
                        if inp == "quit":
                            runningSummary = False
                            continue
                        
                        totalExpense = sum(expense.amount for expense in expenses if expense.date.month == int(inp))
                        print(f"\nTotal expense: {totalExpense:.2f}")
                        for category in Expense.categories:
                            print(f"{category}: {sum(expense.amount for expense in expenses if expense.category == category and expense.date.month == int(inp)  ):.2f}")

            case 6: 
                print("Budget?")
                inp = float(input())
                if(inp < 0): 
                    print("Budget must be greater than 0.")
                    continue
                budget = inp
                storage.updateBudget(budget)


        sleep(2)
        print()

        
        



if __name__ == "__main__":
    main()