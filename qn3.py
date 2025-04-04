def get_number():
    while True:
        try:
            number = float(input("Please enter a number: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Example usage
print(f"You entered: {get_number()}")