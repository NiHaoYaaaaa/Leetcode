from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = {int(s) for s in deadends}
        t = int(target)
        start = 0

        if start in dead or t in dead:
            return -1

        dist = [-1] * 10000
        dist[start] = 0
        dq = deque([start])

        while dq:
            x = dq.popleft()
            if x == t:
                return dist[x]
            w = [(x // 1000) % 10,
                 (x //  100) % 10,
                 (x //   10) % 10,
                 (x      ) % 10]
            for i in range(4):
                for d in (-1, 1):
                    new_w = (w[i] + d) % 10
                    y_int = w[0]*1000 + w[1]*100 + w[2]*10 + w[3] \
                            - w[i]* (10**(3-i)) + new_w * (10**(3-i))
                    if dist[y_int] == -1 and y_int not in dead:
                        dist[y_int] = dist[x] + 1
                        dq.append(y_int)

        return -1