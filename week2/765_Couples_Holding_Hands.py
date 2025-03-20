class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        seat = {value: index for index, value in enumerate(row)}
        count = 0
        n = len(row)
        for i in range(0, n-2, 2):
            a = row[i]
            if a % 2 == 0:
                if row[i + 1] == a + 1:
                    continue
                b_index = seat[a + 1]
                stranger = row[i + 1]
                row[i + 1], row[b_index] = a + 1, stranger
                seat[a + 1], seat[stranger] = i + 1, b_index
                count += 1
            else:
                if row[i + 1] == a - 1:
                    continue
                b_index = seat[a - 1]
                stranger = row[i + 1]
                row[i + 1], row[b_index] = a - 1, stranger
                seat[a - 1], seat[stranger] = i + 1, b_index
                count += 1
        return count