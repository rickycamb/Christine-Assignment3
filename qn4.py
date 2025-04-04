names = ["Alice", "Bob", "Charlie", "Diana"]

# Write names to the file
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

# Read names from the file
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())  # Print each name without newline