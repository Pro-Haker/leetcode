class Solution:
    def areAlmostEqual(self, s1, s2):
        for idx1 in range(len(s1)):
            for idx2 in range(len(s1)):
                list1 = list(s1)
                list2 = list(s2)
                buffer = list1[idx2]
                list1[idx2] = list1[idx1]
                list1[idx1] = buffer
                buffer = list2[idx2]
                list2[idx2] = list2[idx1]
                list2[idx1] = buffer
                swappeds1 = ''.join(list1)
                swappeds2 = ''.join(list2)
                if swappeds1 == s2 or s1 == swappeds2: return True
        return False