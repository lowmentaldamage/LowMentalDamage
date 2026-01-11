# Problem 1
#
# Problem Statement
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6, and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.


# Initialize accumulator to store the sum of valid multiples
total = 0

# Iterate through all natural numbers below 1000 (i.e., 1 to 999)
for i in range(1, 1000):
    # Check if current number is divisible by 3 or 5
    if i % 3 == 0 or i % 5 == 0:
        # Add the number itself (not 1!) to the running total
        total += i

# Output the final result
print(total)  # → 233168