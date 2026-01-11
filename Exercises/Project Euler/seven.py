# Problem 7
#
# 10001st Prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10001st prime number?


# Check if a number is prime
def is_prime(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:     # check divisibility up to sqrt(n)
        if n % i == 0:
            return False
        i += 1

    return True


count = 0      # how many primes we have found
number = 1     # current number to test

while count < 10001:
    number += 1
    if is_prime(number):
        count += 1

print(number)  # the 10001st prime
