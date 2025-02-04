class Solution(object):
    def maxAscendingSum(self, nums):
        sums = []
        sum = 0
        for i in range(len(nums)):
            if nums[i] > nums[i - 1]:
                sum += nums[i]
            else:
                sums.append(sum)
                sum = nums[i]
        sums.append(sum)
        return max(sums)