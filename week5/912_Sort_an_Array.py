class Solution:
    def merge(self, left, right) -> List[int]:
        ans = []
        left_index = right_index = 0
        left_length = len(left)
        right_length = len(right)
        while left_index < left_length and right_index < right_length:
            if left[left_index] < right[right_index]:
                ans.append(left[left_index])
                left_index += 1
            else:
                ans.append(right[right_index])
                right_index += 1
        if left_index == left_length:
            ans.extend(right[right_index:])
        else:
            ans.extend(left[left_index:])
        return ans

    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length <= 1:
            return nums
        middle = length // 2
        left = self.sortArray(nums[:middle])
        right = self.sortArray(nums[middle:])
        ans = self.merge(left, right)
        return ans