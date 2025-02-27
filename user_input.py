# Function to perform the calculation
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:  # Check for division by zero
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"

# Main program
def main():
    print("Simple Calculator")
    print("-----------------")

    try:
        # Input: Get two numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Input: Get the operator from the user
        operator = input("Enter an operator (+, -, *, /): ")

        # Perform the calculation
        result = calculate(num1, num2, operator)

        # Output: Display the result
        if isinstance(result, str):  # If result is a string (error or invalid operator)
            print(result)
        else:
            print(f"{num1} {operator} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values for the numbers.")

# Run the program
if __name__ == "__main__":
    main()
