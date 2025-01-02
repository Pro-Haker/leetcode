class Solution(object):
    def romanToInt(self, s):
        result = 0
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev_char = s[-1]
        for this_char in s[::-1]:
            if this_char == prev_char or romans[this_char] > romans[prev_char]:
                result += romans[this_char]
            else:
                result -= romans[this_char]
            prev_char = this_char
        return result