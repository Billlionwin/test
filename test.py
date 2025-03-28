def sum_of_digits(number):
    """
    Calculate the sum of the digits of a given number.
    :param number: int
    :return: int
    """
    return sum(int(digit) for digit in str(abs(number)))

# Example usage
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"The sum of the digits is: {sum_of_digits(num)}")

# Test cases
def test_sum_of_digits():
    assert sum_of_digits(123) == 6
    assert sum_of_digits(-123) == 6
    assert sum_of_digits(0) == 0
    assert sum_of_digits(9999) == 36
    assert sum_of_digits(-9999) == 36
    assert sum_of_digits(1001) == 2
    assert sum_of_digits(-1001) == 2
    assert sum_of_digits(1234567890) == 45
    assert sum_of_digits(-1234567890) == 45
    assert sum_of_digits(1) == 1
    assert sum_of_digits(-1) == 1
# Run tests
if __name__ == "__main__":
    test_sum_of_digits()
    print("All tests passed!")
