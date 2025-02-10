class Solution(object):
    def clearDigits(self, s):
        slist = list(s)
        digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        finds = [0]
        while max(finds) != -1:
            for digit in digits:
                finds.append(slist.find(digit))
            slist.pop(max(finds))
            idx = max(finds)
            while slist[idx] not in digits:
                idx -= 1
            slist.pop(idx)
        s = "".join(slist)
        return s