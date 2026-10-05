class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        myStack = []
        if not tokens:
            return 0
        
        for x in tokens:
            if x not in {"+", "-", "*", "/"}:
                num = int(x)
                myStack.append(num)
            else:
                num1 = myStack.pop()
                num2 = myStack.pop()
                if x == "+":
                    myStack.append(num1+num2)
                elif x == "-":
                    myStack.append(num2-num1)
                elif x == "*":
                    myStack.append(num1*num2)
                elif x == "/":
                    myStack.append(num2 // num1)
                



        return myStack[-1] 