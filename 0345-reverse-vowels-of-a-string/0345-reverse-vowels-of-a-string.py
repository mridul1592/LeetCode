class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        vwInS = []
        retS = []
        for i in s:
            if i in vowels:
                vwInS.append(i)
        for i,c in enumerate(s):
            if c in vowels:
                retS.append(vwInS[-1])
                vwInS = vwInS[:-1]
            else:
                retS.append(c)


        return ''.join(retS)