from collections import deque
class RecentCounter:

    def __init__(self, duration=3000):
        self.requests = deque()
        self.duration = duration
        self.last_ping = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)

        while self.requests[0] < t - self.duration:
            self.requests.popleft()

        return len(self.requests)

