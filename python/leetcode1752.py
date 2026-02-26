class Solution(object):
    def check(self, nums):
        sorted_nums = sorted(nums)
        rotated_nums = sorted_nums
        for _ in nums:
            rotated_nums.insert(0, rotated_nums.pop())
            if rotated_nums == nums: return True
        return False