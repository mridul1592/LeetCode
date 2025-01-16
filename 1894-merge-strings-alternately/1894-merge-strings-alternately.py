class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        op = ""
        l = min(len(word1), len(word2))
        
        for i in range(l):
            op += word1[i]
            op += word2[i]

        op += word1[l:]
        op += word2[l:]    
        return op