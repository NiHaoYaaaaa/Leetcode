import heapq
class ExamRoom:
    def __init__(self, N: int):
        self.N = N
        self.heap = []
        self.start_map = {} 
        self.end_map = {}    
        self.students = set()

        self.add_interval(-1, N)

    def add_interval(self, i, j):
        if i == -1:
            dist = j
        elif j == self.N:
            dist = self.N - 1 - i
        else:
            dist = (j - i) // 2

        interval = (i, j)
        heapq.heappush(self.heap, (-dist, i, j))
        self.start_map[i] = interval
        self.end_map[j] = interval

    def seat(self) -> int:
        while self.heap:
            _, i, j = heapq.heappop(self.heap)

            if self.start_map.get(i) != (i, j) or self.end_map.get(j) != (i, j):
                continue

            self.start_map.pop(i)
            self.end_map.pop(j)

            if i == -1:
                seat = 0
            elif j == self.N:
                seat = self.N - 1
            else:
                seat = (i + j) // 2

            self.students.add(seat)

            self.add_interval(i, seat)
            self.add_interval(seat, j)

            return seat

    def leave(self, p: int) -> None:
        self.students.remove(p)

        left = None
        right = None

        if p in self.end_map:
            left = self.end_map.pop(p)
            self.start_map.pop(left[0])
        if p in self.start_map:
            right = self.start_map.pop(p)
            self.end_map.pop(right[1])

        i = left[0] if left else p
        j = right[1] if right else p

        self.add_interval(i, j)
