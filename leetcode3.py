class Solution(object):
    def lengthOfLongestSubstring(self, s):
        leftp = 0
        rightp = 0
        lens = []
        usedchars = []
        for i in range(len(s)):
            if s[i] not in usedchars:
                rightp += 1
                usedchars.append(s[i])
            else:
                lens.append(rightp - leftp)
                for _ in range(rightp - leftp + 1): # FIXME
                    leftp += 1                      # THIS LOOP DOESN'T WORK
                    usedchars.pop(0)                # THE VALUE POPPED HERE
                    if s[i] not in usedchars: break # JUST COMES BACK
        lens.append(rightp - leftp + 1)
        return max(lens)