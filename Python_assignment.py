A = int(input("Enter a number: "))

B = int(input("Enter a number: "))

operator = input("Select operator ( + , - , / , *) to perform calculation: ")

if operator == "+" :
    Result = A + B
    print(f"{A} {operator} {B} = {Result}")

elif operator == "-":
    Result = A - B
    print(f"{A} {operator} {B} = {Result}")

elif operator == "/":
    Result = A / B
    print(f"{A} {operator} {B} = {Result}")

elif operator == "*":
    Result = A * B
    print(f"{A} {operator} {B} = {Result}")

else:
    print("Invalid operator! Try again!")

