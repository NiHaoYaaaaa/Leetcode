import bisect
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def can_assign(k):
            task_slice = tasks[:k]
            worker_slice = workers[-k:]
            window = worker_slice[:]
            pills_left = pills

            for task in reversed(task_slice):
                if window and window[-1] >= task:
                    window.pop()
                else:
                    idx = bisect.bisect_left(window, task - strength)
                    if idx == len(window) or pills_left == 0:
                        return False
                    del window[idx]
                    pills_left -= 1
            return True

        left, right = 0, min(len(tasks), len(workers))
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            if can_assign(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return answer