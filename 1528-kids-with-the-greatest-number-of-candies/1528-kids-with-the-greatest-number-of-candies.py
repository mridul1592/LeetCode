class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        op = []
        maxC = max(candies)
        for i in candies:
            if i+extraCandies >= maxC:
                op.append(True)
            else:
                op.append(False)
        
        return op