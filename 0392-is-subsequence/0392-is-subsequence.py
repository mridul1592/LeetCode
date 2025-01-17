class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_char = ''
        s_len = len(s)
        sptr = 0
        ret = False
        if s == "":
            return True

        for i in t:
            if s[sptr] == i:
                sptr += 1
            if sptr == s_len:
                return True
        
        return False
