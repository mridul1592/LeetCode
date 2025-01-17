class Solution:

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n == 1:
            return nums[0]
        if k == 1:
            return max(nums)
        else:
            sum_arr = []
            max_sum = sum(nums[0:k])
            s = max_sum
            print(max_sum)
            for i in range(k, n):
                s = s - nums[i-k] + nums[i]
                if s > max_sum:
                    max_sum = s
        return float(max_sum)/float(k)