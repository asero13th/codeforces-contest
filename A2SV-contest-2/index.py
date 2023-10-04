def longestPalindromeSubsequence(s: str) -> int:
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1

    for i in range(n):
        dp[i][i] = True

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]
def longestPalindromeSubstring(s: str) -> str:
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_length = 1

    # Single character substrings are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for palindromic substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Check for palindromic substrings of length greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_length = length

    return s[start:start + max_length]