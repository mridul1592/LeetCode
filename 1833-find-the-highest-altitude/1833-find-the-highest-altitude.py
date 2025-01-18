class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        alt = [0]
        cur_alt = 0
        for i in gain:
            cur_alt += i
            alt.append(cur_alt)

        return max(alt)