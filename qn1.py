def classify_number():
    while True:
        try:
            number = int(input("Please enter an integer: "))
            if number > 0:
                return "Positive"
            elif number < 0:
                return "Negative"
            else:
                return "Zero"
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Example usage
print(classify_number())