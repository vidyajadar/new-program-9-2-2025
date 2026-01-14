# Define the functions for arithmetic operations
def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers, includes basic error handling for zero division"""
    if y == 0:
        return "Error! Cannot divide by zero."
    return x / y

def calculator():
    # Display the menu of operations to the user
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    while True:
        # Take input from the user
        choice = input("Enter choice (1/2/3/4): ")

        # Check if the choice is valid
        if choice in ('1', '2', '3', '4'):
            try:
                # Prompt the user for two numbers and convert them to floating-point numbers
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue # Restart the loop to ask for input again

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

            # Ask the user if they want to perform another calculation
            next_calculation = input("Do you want to do another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input. Please enter a valid choice (1/2/3/4).")

# Call the calculator function to run the program
if __name__ == "__main__":
    calculator()
