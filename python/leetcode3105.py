class Solution(object):
    def longestMonotonicSubarray(self, nums):
        lengths = []
        lengthinc = 1
        lengthdec = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                lengthinc += 1
            else:
                lengths.append(lengthinc)
                lengthinc = 1
            if nums[i] > nums[i + 1]:
                lengthdec += 1
            else:
                lengths.append(lengthdec)
                lengthdec = 1
        lengths.append(lengthinc)
        lengths.append(lengthdec)
        return max(lengths)