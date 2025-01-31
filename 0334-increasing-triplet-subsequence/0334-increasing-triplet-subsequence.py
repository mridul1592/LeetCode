class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        for i in nums:
            if i < first:
                first = i
            elif i > first and i < second:
                second = i
            elif i > second:
                return True
        
        return False