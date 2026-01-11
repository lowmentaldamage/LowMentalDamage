X = int(input())    # First integer

N = int(input())    # Second integer

together = X * N # How much can he use totally


overall = 0     # Overall value used that month
for i in range(N):
    Mi = int(input())   # Megabytes used in month i
    overall += Mi

print(together - overall + X)


