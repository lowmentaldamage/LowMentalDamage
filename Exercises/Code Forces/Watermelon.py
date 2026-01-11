# Watermelon Division Problem:
# Given the total weight w (1 ≤ w ≤ 100) of a watermelon,
# determine if it can be split into two *positive* parts,
# each with an *even* number of kilos (parts need not be equal).
#
# Observation:
# - Let the parts be a and b, where a + b = w, a > 0, b > 0, and both a and b even.
# - Since even + even = even, w must be even.
# - Additionally, the smallest possible even positive parts are 2 and 2 → w ≥ 4.
# → Therefore, answer is "YES" if and only if w is even and w ≥ 4.
#   (i.e., w % 2 == 0 and w > 2)

w = int(input().strip())
print("YES" if w > 2 and w % 2 == 0 else "NO")