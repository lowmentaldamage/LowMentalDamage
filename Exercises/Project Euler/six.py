# Sum Square Difference - Problem 6
#
# The sum of the squares of the first ten natural numbers is:
#     1² + 2² + ... + 10² = 385
#
# The square of the sum of the first ten natural numbers is:
#     (1 + 2 + ... + 10)² = 55² = 3025
#
# Hence, the difference between the sum of the squares and the square of the sum is:
#     3025 - 385 = 2640
#
# Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum.


# Sum of squares
sum = 0
for i in range(1,101):
    sum += (i**2)
sum1 = sum


# Square of sum
together = 0
for i in range(1,101):
    together += i
squared = together ** 2 # Final integer


# Calculate together
difference = squared - sum1
print(difference)




    