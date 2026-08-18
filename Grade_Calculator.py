for Grade in range(1, 4):
    score = float(input(f"Enter the score for Grade {Grade}: "))
    if score >= 90:
        print("Grade A")
    elif score >= 80:
        print("Grade B")
    elif score >= 70:
        print("Grade C")
    elif score >= 60:
        print("Grade D")
    else:
        print("Grade F")