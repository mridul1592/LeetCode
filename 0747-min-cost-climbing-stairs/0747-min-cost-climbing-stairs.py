class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        top = len(cost)

        dp = [0] * (top+1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        cost = cost + [0]

        for i in range(2, top+1):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return dp[top]

