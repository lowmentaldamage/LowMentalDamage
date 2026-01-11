# ...existing code...
class Solution:
  def isPalindrome(self, x: int) -> bool:
    # Negative numbers are not palindromes because of the leading '-'
    if x < 0:
      return False

    # 'rev' will store the reversed digits of x
    rev = 0
    # Use a copy 'y' so the original input 'x' remains unchanged for comparison
    y = x

    # Construct the reversed integer by iteratively taking the last digit of y
    while y:
      # Append the last digit of y to rev
      rev = rev * 10 + y % 10
      # Remove the last digit from y (integer division)
      y //= 10

    # x is a palindrome if reversing its digits yields the same number
    return rev == x
# ...existing code...