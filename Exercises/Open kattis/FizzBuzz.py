# How it works:
# - Print integers from 1 to N (inclusive), one per line.
# - If a number is divisible by X → print "Fizz"
# - If a number is divisible by Y → print "Buzz"
# - If a number is divisible by both X and Y → print "FizzBuzz"
# - Otherwise, print the number itself.

# Input:
# - Single test case on one line: three integers X, Y, N (1 <= X < Y <= N <= 100)

# Output:
# - Print N lines: each line contains either "Fizz", "Buzz", "FizzBuzz", or the number.

# Sample Input 1: 2 3 7
# Output:
# 1
# Fizz
# Buzz
# Fizz
# 5
# FizzBuzz
# 7


# Single test case input for X, Y, N
X, Y, N = map(int, input().split())


# Printing out as many times as N says
for i in range(1,N+1):

    if i % X == 0 and i % Y == 0: # Checking dividibility by X,Y
        print("FizzBuzz")

    elif i % X == 0: # Checking for X
        print("Fizz")

    elif i % Y == 0: # Checking for Y
        print("Buzz")

    else:
        print(i)

