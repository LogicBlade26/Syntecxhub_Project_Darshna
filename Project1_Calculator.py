history = []
def cal(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error"
        return num1 / num2
    elif operator == "%":
        if num2 == 0:
            return "Error"
        return num1 % num2
    elif operator == "**":
        return num1 ** num2
    else:
        return "Invalid operator"
def show_history():
    if not history:
        print("No Calculations")
        return
    print("---- HISTORY ----")
    for calculation in history:
        print(calculation)
def menu():
    while True:
        print("\n1. Calculate")
        print("2. Show history")
        print("3. Clear history")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                num1 = float(input("Enter first number: "))
                print("Operators: +  -  *  /  %  **")
                operator = input("Enter the operator: ")
                num2 = float(input("Enter second number: "))
                result = cal(num1, num2, operator)
                if isinstance(result, str):
                    print(result)
                else:
                    calculation = f"{num1} {operator} {num2} = {result}"
                    print(f"Result: {result}")
                    history.append(calculation)
            except ValueError:
                print("Error: Please enter valid numbers.")
        elif choice == "2":
            show_history()
        elif choice == "3":
            history.clear()
            print("History cleared")
        elif choice == "4":
            print("Thank You")
            break
        else:
            print("Invalid choice")
menu()