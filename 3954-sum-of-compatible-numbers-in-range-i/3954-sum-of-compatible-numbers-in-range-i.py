class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        #Creating a list to store all compatible x values 
        compatible = []

        #looping through (max(n-k,1), n+K+1) to collect compatible x values
        for x in range(max(n-k,1), n+k+1):
            if abs(n-x)<=k and n&x==0: #applying given condition
                compatible.append(x) #append compatible x value to thr list

        ans = 0 #Initialinzing a variable with value 0 
        for i in compatible :
            ans += i #adding values
        return ans #returning the total sum of all compatible values
        #End of the program

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna