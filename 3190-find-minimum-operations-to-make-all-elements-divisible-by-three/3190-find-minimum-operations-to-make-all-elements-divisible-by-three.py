class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if i%3 != 0:
                count+=1
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna