class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = 1
        count = 1
        cur_high = 1
        turn = False

        j = 1
        while j < n and ratings[j] == ratings[j-1]:
            candy += 1
            j += 1
        if j == n:
            return candy

        up = True if ratings[j] > ratings[j-1] else False
        for i in range(j,n):
            if ratings[i] == ratings[i-1]:
                if count >= cur_high and turn and not up:
                        candy += count - cur_high + 1
                candy += 1
                count = 1
                cur_high = 1
                turn = False
                if i+1 < n:
                    up = True if ratings[i+1] > ratings[i] else False
                continue
            if up:
                if ratings[i] > ratings[i-1]:
                    count += 1
                    candy += count
                else:
                    cur_high = count
                    count = 1
                    candy += count
                    up = False
                    turn = True
            else:
                if ratings[i] < ratings[i-1]:
                    count += 1
                    candy += count
                    if i == n-1:
                        if count >= cur_high and turn:
                            candy += count - cur_high + 1
                else:
                    if count >= cur_high and turn:
                        candy += count - cur_high + 1
                        cur_high = 2
                    count = 2
                    candy += count
                    up = True
        return candy
                