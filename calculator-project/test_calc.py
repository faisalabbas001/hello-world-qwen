"""Simple tests for the calculator functions."""
from calc import add, subtract, multiply, divide, calculate_all_operations


def test_calculations():
    """Test all calculation functions."""
    print("Running tests...")
    
    # Test addition
    assert add(5, 3) == 8
    assert add(-2, 2) == 0
    assert add(0, 0) == 0
    print("✓ Addition tests passed")
    
    # Test subtraction
    assert subtract(5, 3) == 2
    assert subtract(2, 5) == -3
    assert subtract(0, 0) == 0
    print("✓ Subtraction tests passed")
    
    # Test multiplication
    assert multiply(5, 3) == 15
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0
    print("✓ Multiplication tests passed")
    
    # Test division
    assert divide(6, 3) == 2
    assert divide(7, 2) == 3.5
    assert divide(0, 5) == 0
    print("✓ Division tests passed")
    
    # Test division by zero
    try:
        divide(5, 0)
        assert False, "Should raise ZeroDivisionError"
    except ZeroDivisionError:
        print("✓ Division by zero correctly handled")
    
    # Test calculate_all_operations
    results = calculate_all_operations(10, 5)
    assert results["addition"] == 15
    assert results["subtraction"] == 5
    assert results["multiplication"] == 50
    assert results["division"] == 2.0
    print("✓ All operations test passed")
    
    print("\nAll tests passed successfully! ✅")


if __name__ == "__main__":
    test_calculations()