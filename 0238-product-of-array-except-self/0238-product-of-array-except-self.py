class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [None] * l
        prefix_prd = 1
        postfix_prd = 1

        for i in range(l):
            res[i] = prefix_prd
            prefix_prd *= nums[i]
        for i in range(l-1, -1, -1):
            res[i] *= postfix_prd
            postfix_prd *= nums[i]
        return res