# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def percentage(total, value):
    if total == 0:
        return "Error! Total cannot be zero."
    return (value / total) * 100


#here how can we use the calculator module in another program or file

# main.py

# import calculator

# # Sample numbers
# num1 = 10
# num2 = 5

# # Perform calculations using the calculator module
# print(f"Addition of {num1} and {num2}: {calculator.add(num1, num2)}")
# print(f"Subtraction of {num2} from {num1}: {calculator.subtract(num1, num2)}")
# print(f"Multiplication of {num1} and {num2}: {calculator.multiply(num1, num2)}")
# print(f"Division of {num1} by {num2}: {calculator.divide(num1, num2)}")
# print(f"Percentage of {num2} in {num1}: {calculator.percentage(num1, num2)}")

#written by zala nirbhay(TY-BCA)