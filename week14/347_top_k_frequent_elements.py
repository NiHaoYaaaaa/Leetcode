import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ans = [item for item, freq in heapq.nlargest(k, count.items(), key=lambda x: x[1])]
        return ans