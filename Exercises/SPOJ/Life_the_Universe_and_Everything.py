# Input number 1
n = int(input())

values = [] # Saved values

# check if number is 43, if it is break the loop else continioue
while n != 42:
    values.append(n)
    n = int(input())

a = 0
for num in range(len(values)):
    print(values[a])
    a += 1
