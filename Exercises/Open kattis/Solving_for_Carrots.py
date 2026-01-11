"""
Kattis - Solving for Carrots

Read two integers N and P. Then read N lines describing contestants (these
description lines are irrelevant to the answer). The number of carrots
handed out equals P (one carrot per huffle-puff problem solved).

Example:
Input:
2 1
carrots?
bunnies

Output:
1
"""

N, P = map(int, input().split())

for i in range(N):
    a = input()
print(P)
