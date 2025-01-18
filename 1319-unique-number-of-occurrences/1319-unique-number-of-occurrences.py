class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashMap = {}
        for i in arr:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] += 1

        len_hash = len(hashMap)
        set1 = set(hashMap.values())
        len_set = len(set1)
        if len_hash == len_set:
            return True
        else:
            return False