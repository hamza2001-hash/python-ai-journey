for i in range(5):
    expense += float(input(f"Enter expense {i + 1}: "))

print(f"Total expenses: ${expense:.2f}")
print(f"Average expense: ${expense / 5:.2f}")