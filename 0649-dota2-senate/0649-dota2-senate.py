class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        Rq = deque()
        Dq = deque()

        for i, ele in enumerate(senate):
            if ele == 'R':
                Rq.append(i)
            else:
                Dq.append(i)
        print(Rq, Dq)
        while Rq and Dq:
            R = Rq.popleft()
            D = Dq.popleft()
            if R < D:
                Rq.append(R+n)
            else:
                Dq.append(D+n)
        
        if not Rq: 
            return 'Dire'
        else:
            return 'Radiant'

