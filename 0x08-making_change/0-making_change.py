def makeChange(coins, total):
    # If the total is 0 or less, no coins are needed
    if total <= 0:
        return 0
    
    # Initialize dp array with "infinity" (a large number).
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins are needed to make total of 0
    
    # For each coin, update the dp array.
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[total] is still infinity, it means the total cannot be formed.
    if dp[total] == float('inf'):
        return -1
    
    return dp[total]
