def min_cost_break_chocolate(m, n, x, y):
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        dp[i][1] = sum(x[:i-1])
    for j in range(1, n+1):
        dp[1][j] = sum(y[:j-1])

    for i in range(2, m+1):
        for j in range(2, n+1):
            dp[i][j] = min(dp[i-1][j] + x[i-2], dp[i][j-1] + y[j-2], dp[i-1][j-1] + x[i-2] + y[j-2])

    return dp[m][n]

# Example usage
num_test_cases = int(input())
for _ in range(num_test_cases):
    m, n = map(int, input().split())
    x = [int(input()) for _ in range(m-1)]
    y = [int(input()) for _ in range(n-1)]
    print(min_cost_break_chocolate(m, n, x, y))
