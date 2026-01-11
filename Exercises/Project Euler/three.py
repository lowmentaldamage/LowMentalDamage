# Problem 3
#
# Largest Prime Factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?


# Define the number
n = 600851475143

def largest_prime_factor(n):
    largest = None

    while n % 2 == 0:
        largest = 2
        n //= 2

    i = 3
    while i * i <= n:
        while n % i == 0:
            largest = i
            n //= i
        i += 2

    if n > 1:
        largest = n

    return largest

print(largest_prime_factor(n))
