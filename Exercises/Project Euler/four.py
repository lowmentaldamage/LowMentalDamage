# Problem 4
#
# Largest Palindrome Product
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


number = 0
palindrome = []
start = 0
for j in range(999):
    for k in range(999):
        number = j * k
        str_number = str(number)
        reversed_number = str_number[::-1]
        if str_number == reversed_number:
            palindrome.append(number)

a = set(palindrome)
sorted_set = sorted(a, reverse=True)

# Largest palindrome made from the product of two 3-digit numbers
print(sorted_set[0]) # 0 is first