from collections import deque
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key = lambda x : x[1])
        n = len(intervals)
        dq = deque()
        dq.append(intervals[0][1] - 1)
        dq.append(dq[0] + 1)
        for i in range(1, n):
            if intervals[i][0] > dq[-1]:
                dq.append(intervals[i][1]-1)
                dq.append(intervals[i][1])
            elif dq[-1] < intervals[i][1]:
                if dq[-2] >= intervals[i][0]:
                    continue
                else:
                    dq.append(intervals[i][1])
            elif dq[-1] == intervals[i][1]:
                if intervals[i][0] > dq[-2]:
                    dq.append(dq[-1])
                    dq[-2] = dq[-1] - 1
        return len(dq)
            


            