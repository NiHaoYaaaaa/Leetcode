class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        head = 0
        end = len(people) - 1
        num = 0
        while(head < end):
            if (people[head] + people[end]) > limit:
                num += 1
                head += 1
            else:
                num += 1
                head += 1
                end -= 1
        if(head == end):
            num += 1
        return num