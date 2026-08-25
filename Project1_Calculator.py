history=[]
def calculator(num1, num2, operator):
    if operator=="+":
        return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="*":
        return num1*num2
    elif operator=="/":
        if num2==0:
            return "Error"
        return num1/num2
    elif operator=="%":
        if num2==0:
            return "Error"
        return num1%num2
    elif operator=="**":
        return num1**num2
    else:
        return "Invalid"
def show_history():
    if not history:
        print("No Calculations")
        return
    print("----HISTORY----")
    for cal in history:
        print(cal)
def cal():
    while True:
        print("1. Calculate")
        print("2. Show history")
        print("3. Clear history")
        print("4. Exit")
        choice=input("Enter your choice:")
        if choice=='1':
            try:
                num1=float(input("Enter first number:"))
                print("Operators: + - * / % **")
                operator=input("Enter the operator:")
                num2=float(input("Enter second number:"))
                result=cal(num1,operator,num2)
                if isinstance(result, str):
                    print(result)
                else:
                    cal=f"{num1} {operator} {num2} = {result}"
                    print(f"Result: {result}")
                history.append(cal)
            except ValueError:
                print("Error")
        elif choice=="2":
            show_history()
        elif choice=="3":
            history.clear()
            print("History cleared")
        elif choice=="4":
            print("Thank You")
            break
        else:
            print("Invalid choice")
calculator()