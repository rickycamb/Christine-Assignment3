def calculate_average(*args):
    """
    Calculate the average of a variable number of arguments.

    Parameters:
    *args: A variable number of numerical arguments.

    Returns:
    float: The average of the provided numbers.
    """
    if not args:
        return 0  # Return 0 if no numbers are provided
    return sum(args) / len(args)

# Example usage
print(calculate_average(10, 20, 30))  # Output: 20.0