class Solution:
    def areAlmostEqual(self, s1, s2):
        if s1 == s2: return True
        changes = 0
        idxs = []
        for idx in range(len(s1)):
            if s1[idx] != s2[idx]:
                changes += 1
                idxs.append(idx)
        if changes != 2: return False
        if s1[idxs[0]] != s2[idxs[1]]: return False
        if s2[idxs[0]] != s1[idxs[1]]: return False
        return True