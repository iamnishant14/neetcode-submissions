class Solution:
    def evals(self,first,second,counter):
        if counter =='/':
            return int(float(first)/second) if second !=0 else 0
        elif counter == '*':
            return first*second
        elif counter == '+':
            return first+second
        else:
            return first-second
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        opr = ['/','*','+','-']
        for token in tokens:
            if token in opr:
                second,first=stack.pop(),stack.pop()
                result = self.evals(first,second,token)
                stack.append(result)
            else:
                stack.append(int(token))
            print(stack)
        return stack[0]