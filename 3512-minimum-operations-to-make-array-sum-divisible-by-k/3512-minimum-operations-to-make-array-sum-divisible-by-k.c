int minOperations(int* nums, int numsSize, int k) {
    int sum =0;
    for(int i=0;i<numsSize;i++){
        sum=sum+nums[i];
    }
    return sum%k;
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna