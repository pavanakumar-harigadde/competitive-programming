class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans=[]
        for i in range(len(matrix)):
            degree=0
            for j in range(len(matrix)):
                if matrix[i][j]==1:
                    degree+=1
            ans.append(degree)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna