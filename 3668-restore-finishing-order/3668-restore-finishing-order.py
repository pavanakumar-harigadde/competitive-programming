class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        arr=[]
        for i in order:
            if i in friends:
                arr.append(i)

        return arr

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna