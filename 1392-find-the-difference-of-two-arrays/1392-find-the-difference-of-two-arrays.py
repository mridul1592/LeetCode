class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        res1 = [x for x in set1 if x not in set2]
        res2 = [x for x in set2 if x not in set1]
        return [res1, res2]
