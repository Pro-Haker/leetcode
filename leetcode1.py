class Solution(object):
    def twoSum(self, nums, target):
        length = range(len(nums))
        for i in length:
            for j in length:
                if nums[i] + nums[j] == target and i > j:
                    return i, j