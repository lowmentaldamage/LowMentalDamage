# ...existing code...
class Solution(object):
    def twoSum(self, nums, target):
        # d maps a value -> its index in nums (for values seen so far)
        d = {}
        # Iterate once, checking for the required complement for each element
        for i, n in enumerate(nums):
            # complement needed to reach target with current number n
            complement = target - n
            # If complement was already seen, we found the pair
            if complement in d:
                return [d[complement], i]
            # Otherwise record the current number's index for future checks
            d[n] = i

# Example usage (unchanged)
nums = list(range(1, 101))
target = 172
print(Solution().twoSum(nums, target))