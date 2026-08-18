balance = 1000
amount = float(input("Enter the amount you want to withdraw: "))

if amount > balance:
    print("Insufficient funds!")
else:
    balance -= amount
    print(f"Withdrawal successful! Your new balance is: ${balance:.2f}")