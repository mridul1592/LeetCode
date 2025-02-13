from collections import Counter
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        nSum = []
        for i in nums:
            nSum.append(sum([int(a) for a in list(str(i))]))

        maxSum = -1
        c = Counter(nSum)
        countFlag = 1
        
        
        elegSum = []

        for i in c:
            if c[i] > 1:
                elegSum.append(i)

        sumDict = dict()

        for s in elegSum:
            for i in range(len(nums)):
                if nSum[i] == s and s not in sumDict:
                    sumDict[s] = [nums[i]]
                    sumDict[s] += [0]
                elif nSum[i] == s and s in sumDict:
                    if sumDict[s][0] <= nums[i]:
                        sumDict[s][1] = sumDict[s][0]
                        sumDict[s][0] = nums[i]
                    elif sumDict[s][0] > nums[i] and nums[i] > sumDict[s][1]:
                        sumDict[s][1] = nums[i]
                        

        for i in sumDict:
            maxSum = max(sumDict[i][0] + sumDict[i][1], maxSum)

        return maxSum
