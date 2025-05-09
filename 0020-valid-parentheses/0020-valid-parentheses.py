class Solution:
    def isValid(self, s: str) -> bool:
        opening_brackets = ['(','{','[']
        closing_brackets = [')','}',']']
        brackets_dic = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in opening_brackets:
                stack.append(char)
            elif char in closing_brackets:
                if len(stack)==0 or stack[-1]!=brackets_dic[char]:
                    return False
                stack.pop()

        return len(stack)==0