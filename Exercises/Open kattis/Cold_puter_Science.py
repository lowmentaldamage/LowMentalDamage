# We're not going to sugar-coat it: Chicago’s winters can be rough.
# The temperatures sometimes dip to uncomfortable levels and, after last year’s “polar vortex”,
# the University of Chicago Weather Service wants to find out exactly how bad the winter was.
# More specifically, they are interested in knowing the total number of days in which the temperature was below zero degrees Celsius.

# Input:
# - First line: single positive integer n (1 <= n <= 100) — number of temperatures collected.
# - Second line: n integers separated by spaces — each temperature t (-1000000 <= t <= 1000000).

# Output:
# - Print a single integer: count of temperatures strictly less than zero.

# Sample Input 1:
# 3
# 5 -10 15
# → Output: 1

# Sample Input 2:
# 5
# -14 -5 -39 -5 -7
# → Output: 5


# Positive integer n
n = int(input())

# n temperatures, each separated by a single space.
temparatures = map(int, input().split())

 # Check each number to see if its less than 0
number_under_zero = 0
for temp in temparatures:
    if temp < 0:
        number_under_zero += 1

print(number_under_zero)

