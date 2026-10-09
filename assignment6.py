def knapsack_bottom_up(values, weights, W):
    n = len(values)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


def knapsack_top_down(values, weights, n, W, dp):
    if n == 0 or W == 0:
        return 0

    if dp[n][W] != -1:
        return dp[n][W]

    if weights[n - 1] > W:
        dp[n][W] = knapsack_top_down(values, weights, n - 1, W, dp)
    else:
        include = values[n - 1] + knapsack_top_down(
            values, weights, n - 1, W - weights[n - 1], dp
        )
        exclude = knapsack_top_down(
            values, weights, n - 1, W, dp
        )
        dp[n][W] = max(include, exclude)

    return dp[n][W]


values = [60, 100, 120]
weights = [10, 20, 30]
W = 50

n = len(values)

bottom_up_result = knapsack_bottom_up(values, weights, W)

dp = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

top_down_result = knapsack_top_down(values, weights, n, W, dp)

print("Values:", values)
print("Weights:", weights)
print("Capacity:", W)
print("Maximum value using Bottom-Up:", bottom_up_result)
print("Maximum value using Top-Down:", top_down_result)
