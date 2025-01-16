class Solution(object):
    def get_gcd(self, a, b):
        if b == 0:
            return a
        if a%b == 0:
            return b
        else:
            return self.get_gcd(b, a%b)

    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        op = ""
        if str1+str2 == str2+str1 :         
            max_len = self.get_gcd(max(len(str1), len(str2)), min(len(str1), len(str2)))
            op = str1[:max_len]

        else :
            return op
        return op