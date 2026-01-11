# Bit++ Problem:
# Variable x starts at 0.
# Each line is a statement: one of "X++", "++X", "X--", "--X".
# "++" increases x by 1; "--" decreases x by 1.
# Read n statements and compute final value of x.
#--------------------------------------------------------------------------------
# Inputing the value we want
n = int(input())

# Setting x value to zero
x = 0

for _ in range(n):
    statement = input().strip() # Read one statement, e.g., "X++"

    if "++" in statement: # Check if its +1
        x += 1
    elif "--" in statement: # Check if its -1
        x -= 1


# Printing out the results
print(x)
