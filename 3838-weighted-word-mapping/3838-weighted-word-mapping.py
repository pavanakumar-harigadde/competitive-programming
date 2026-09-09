class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result=[]

        for word in words:
            word_weight = sum(weights[ord(char) - ord('a')] for char in word)

            remainder = word_weight % 26

            mapped_char = chr(ord('z') - remainder)

            result.append(mapped_char)

        return "".join(result)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna