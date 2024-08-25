def add (x, y):
    return x + y

def multiply (x, y):
    return x * y

def divide (x, y):
    return (x / y)

def subtract (x, y):
    return x - y

def modulus (x, y):
    return (x // y)

print("Select operation.")
print("1.Add")
print("2.Multiply")
print("3.Divide")
print("4.Subtract")
print("5.Modulus")

while True:
    user_Input = input("Select the operation 1/2/3/4/5: ")

    if user_Input in ("1", "2", "3", "4", "5"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        

        if user_Input == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif user_Input == '2':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif user_Input == '3':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif user_Input == '4':
            print(num1, "-", num2, "=", subtract(num1, num2))
        
        elif user_Input == "5":
            print(num1, "//", num2, "=", modulus(num1, num2))

        next_calcuation = input("Want to perform more Calculations? (yes/no): ")
        if next_calcuation == "no":
            break   
    else:
        print("Invalid Operation")