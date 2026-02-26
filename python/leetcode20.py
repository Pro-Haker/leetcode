class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if char == "(": stack.append(char)
            elif char == "{": stack.append(char)
            elif char == "[": stack.append(char)
            elif char == ")" and stack == []: return False
            elif char == "}" and stack == []: return False
            elif char == "]" and stack == []: return False
            elif char == ")" and stack[-1] == "(": stack.pop()
            elif char == "}" and stack[-1] == "{": stack.pop()
            elif char == "]" and stack[-1] == "[": stack.pop()
            else: return False
        if stack == []: return True
        return False