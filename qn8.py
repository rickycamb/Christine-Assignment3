import random

def generate_random_integers(n, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(n)]

def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# Generate 10 random integers between 1 and 100
random_numbers = generate_random_integers(10, 1, 100)
average = calculate_average(random_numbers)

print(f"Random Numbers: {random_numbers}")
print(f"Average: {average}")