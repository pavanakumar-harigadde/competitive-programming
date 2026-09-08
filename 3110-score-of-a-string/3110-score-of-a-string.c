int scoreOfString(char* s) {
    int ans = 0;

    for(int i=0;i<strlen(s)-1;i++){
        ans+= abs(s[i]-s[i+1]);
    }
    return ans;
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna