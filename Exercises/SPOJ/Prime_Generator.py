# PRIME1 - Prime Generator
# Task: Generate all prime numbers between two given numbers m and n (inclusive) for multiple test cases.
# This is a number theory problem.

# Input Format:
# - First line: t (number of test cases, where t <= 10)
# - Next t lines: each contains two integers m and n (1 <= m <= n <= 1000000000, and n - m <= 100000), separated by a space.

# Output Format:
# - For each test case, print all prime numbers p such that m <= p <= n, one per line.
# - Separate output for different test cases with an empty line.

# Example:
# Input:
#   2
#   1 10
#   3 5
# Output:
#   2
#   3
#   5
#   7
#
#   3
#   5

# Important Note:
# - The input/output can be large. Ensure your algorithm is efficient (e.g., use segmented sieve or optimized trial division).
# - Most languages should handle this if the algorithm is well-designed.
# PRIME1 - Prime Generator
# Task: Generate all prime numbers between two given numbers m and n (inclusive) for multiple test cases.

# Input Format:
# - First line: t (number of test cases, where t <= 10)
# - Next t lines: each contains two integers m and n (1 <= m <= n <= 1000000000, and n - m <= 100000), separated by a space.

# Output Format:
# - For each test case, print all prime numbers p such that m <= p <= n, one per line.
# - Separate output for different test cases with an empty line.

def is_prime_number(n):  # returns True or False for any integer
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


# Number of lines for m, n input
t = int(input())


for i in range(t): # Do as many repeating cycles as variable t wants
    m , n = map(int, input().split())

    #
    for j in range(m,n):
        if is_prime_number(j):
            print(j)
    print()


#_-_-__-_____-----___--_-----_-__--_____-__-----_-_---__--__---__--_-_-_-_---_---_--_
import sys
import math

input = sys.stdin.readline

t = int(input())

# Precompute primes up to sqrt(1e9)
LIMIT = 31623
is_prime = [True] * (LIMIT + 1)
is_prime[0] = False
is_prime[1] = False

primes = []
for i in range(2, LIMIT + 1):
    if is_prime[i]:
        primes.append(i)
        if i * i <= LIMIT:
            for j in range(i * i, LIMIT + 1, i):
                is_prime[j] = False

while t > 0:
    t -= 1

    m, n = map(int, input().split())

    segment = [True] * (n - m + 1)

    if m == 1:
        segment[0] = False

    for p in primes:
        if p * p > n:
            break

        start = max(p * p, ((m + p - 1) // p) * p)

        for j in range(start, n + 1, p):
            segment[j - m] = False

    for i in range(n - m + 1):
        if segment[i]:
            print(m + i)

    print()

