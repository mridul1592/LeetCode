# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        if guess(r) == 0:
            return r
        if guess(l) == 0:
            return l
        while l <= r:
            m = (l+r)//2
            guess_res = guess(m)
            if guess_res == 0:
                return int(m)
            if guess_res == -1:
                r = m
            elif (guess_res == 1):
                l = m
