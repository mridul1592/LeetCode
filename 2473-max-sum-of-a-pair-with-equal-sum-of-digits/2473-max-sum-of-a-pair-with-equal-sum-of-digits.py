from collections import Counter
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        nSum = []
        for i in nums:
            nSum.append(sum([int(a) for a in list(str(i))]))

        maxSum = 0
        c = Counter(nSum)
        countFlag = 1
        for i in c.values():
            if i > 1:
                countFlag = 0
                break
        if countFlag == 1:
            return -1
        
        elegSum = []

        for i in c:
            if c[i] > 1:
                elegSum.append(i)

        sumDict = dict()

        for s in elegSum:
            for i in range(len(nSum)):
                if nSum[i] == s and s not in sumDict:
                    sumDict[s] = [nums[i]]
                elif nSum[i] == s and s in sumDict:
                    sumDict[s] += [nums[i]]


        for i in sumDict:
            sumDict[i].sort(reverse=True)

        for i in sumDict:
            maxSum = max(sumDict[i][0] + sumDict[i][1], maxSum)

        return maxSum