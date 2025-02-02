class Solution:
    def isArraySpecial(self, nums):
        for index in range(len(nums) - 1):
            num1 = nums[index]
            num2 = nums[index + 1]
            parity1 = num1 % 2
            parity2 = num2 % 2
            if parity1 == parity2:
                return False
        return True