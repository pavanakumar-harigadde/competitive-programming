class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n<=2:
            return n
        min_index=nums.index(min(nums))
        max_index=nums.index(max(nums))
        i=min(min_index,max_index)
        j=max(min_index,max_index)

        return min(j+1, n-i, (i+1)+(n-j))

        #Both from left : j+1
        #Both from right: n-i
        #From both sides: (i+1)+(n-j)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna