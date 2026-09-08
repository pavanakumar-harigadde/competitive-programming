int digitFrequencyScore(int n) {
    int result=0;
    if(n<0){
        n=-n;
    }

    while(n>0){
        result+=n%10;
        n/=10;
    }

    return result;
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna