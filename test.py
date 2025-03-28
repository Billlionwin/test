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