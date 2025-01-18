class RecentCounter:

    def __init__(self):
        self.dq = deque()

    def ping(self, t: int) -> int:
        dq = self.dq
        dq.append(t)
        while dq[0] + 3000 < t:
            dq.popleft()

        return len(dq)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
