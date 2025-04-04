# List of temperatures in Celsius
celsius_temperatures = [0, 20, 37, 100]

# Convert to Fahrenheit using lambda and map
fahrenheit_temperatures = list(map(lambda c: c * 9/5 + 32, celsius_temperatures))

# Print the converted list
print(f"Fahrenheit temperatures: {fahrenheit_temperatures}")