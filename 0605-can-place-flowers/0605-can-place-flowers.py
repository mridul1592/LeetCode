class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                is_empty_left = (i == 0) or (flowerbed[i-1] == 0)
                is_empty_right = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)

                if is_empty_left and is_empty_right:
                    flowerbed[i] = 1
                    count +=1
                    if count >= n:
                        return True
        return count >= n