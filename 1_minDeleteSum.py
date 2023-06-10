def minimumDeleteSum(s1, s2):
    m, n = len(s1), len(s2)
    
    # Create a table to store the minimum ASCII sum
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the table
    for i in range(m - 1, -1, -1):
        dp[i][n] = dp[i + 1][n] + ord(s1[i])  # Add ASCII value of s1 character
        
    for j in range(n - 1, -1, -1):
        dp[m][j] = dp[m][j + 1] + ord(s2[j])  # Add ASCII value of s2 character
        
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = min(dp[i + 1][j] + ord(s1[i]), dp[i][j + 1] + ord(s2[j]))
    
    return dp[0][0]  # Return the minimum ASCII sum for the entire strings


s1 = "sea"
s2 = "eat"
result = minimumDeleteSum(s1, s2)
print(result)  # Output: 231 
