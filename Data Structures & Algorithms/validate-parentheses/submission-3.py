class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        append_list = ['(','{','[']
        pop_list = [')','}',']']
        for char in s:
            if char in append_list:
                stack.append(char)
            elif char in pop_list:
                if not stack or append_list[pop_list.index(char)] != stack.pop():
                    return False
        return len(stack)==0