expenses = []

for i in range(5):
    expense = float(input(f"Enter expense {i + 1}: "))
    expenses.append(expense)

print(f"Total expenses: ${sum(expenses):.2f}")
print(f"Average expense: ${sum(expenses) / 5:.2f}")
print(f"Highest expense: ${max(expenses):.2f}")
print(f"Lowest expense: ${min(expenses):.2f}")