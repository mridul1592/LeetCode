class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftW = 0
        rightW = len(height) - 1
        maxA = 0
        while leftW < rightW:
            area = (rightW - leftW) * min(height[leftW], height[rightW])
            maxA = max(maxA, area)

            if height[leftW] <= height[rightW]:
                leftW += 1
            else:
                rightW -= 1

        return maxA