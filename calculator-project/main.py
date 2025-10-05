from calc import add, subtract, multiply, divide, calculate_all_operations


def main():
    print("Calculator Project - Arithmetic Operations jaklsdjaklsdjaskldjaskldjaskldjaskldjaskljkljaskld")
    print("=" * 40)
    
    # Example calculations
    num1 = 15
    num2 = 5
    
    print(f"Numbers: {num1} and {num2}")
    print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
    print(f"Subtraction: {num1} - {num2} = {subtract(num1, num2)}")
    print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")
    print(f"Division: {num1} / {num2} = {divide(num1, num2)}")
    
    print("\nUsing calculate_all_operations function:")
    results = calculate_all_operations(num1, num2)
    for operation, result in results.items():
        print(f"{operation.capitalize()}: {result}")
    
    # Example with different numbers
    print("\n" + "=" * 40)
    print("Another example with different numbers:")
    num3 = 10
    num4 = 3
    
    print(f"Numbers: {num3} and {num4}")
    print(f"Addition: {num3} + {num4} = {add(num3, num4)}")
    print(f"Subtraction: {num3} - {num4} = {subtract(num3, num4)}")
    print(f"Multiplication: {num3} * {num4} = {multiply(num3, num4)}")
    print(f"Division: {num3} / {num4} = {divide(num3, num4):.2f}")
    
    # Example of division by zero handling
    print("\n" + "=" * 40)
    print("Division by zero example:")
    try:
        result = divide(10, 0)
        print(f"10 / 0 = {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
