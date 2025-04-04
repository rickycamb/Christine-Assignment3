class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError("The number is negative.")

# Demonstration
try:
    check_positive(-5)
except NegativeNumberError as e:
    print(e)  # Output: The number is negative.