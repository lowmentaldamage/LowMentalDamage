# Problem 10
#
# Summation of Primes
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.




# MY CODE

sum_primes = 0

for i in range(2, 2_000_000):  # start from 2, since 0 and 1 are not prime
    total_divisions = 0
    for divider in range(1, i + 1):
        if i % divider == 0:
            total_divisions += 1
        if total_divisions > 2:  # not prime if more than 2 divisors
            break
    if total_divisions == 2:  # exactly divisible by 1 and itself
        sum_primes += i

print(sum_primes)







limit = 2_000_000
is_prime = [True] * limit
is_prime[0] = is_prime[1] = False

for i in range(2, int(limit ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, limit, i):
            is_prime[j] = False

sum_primes = sum(i for i, prime in enumerate(is_prime) if prime)
sum_primes