class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        myDict = {"{":"}", 
                "(": ")", 
                "[":"]"}


        for ch in s:
            if ch in myDict:
                myStack.append(ch)
            else:
                if not myStack:
                    return False
                top = myStack.pop()
                if myDict[top] != ch:
                    return False
                
      

        #print(myStack)
        
        
        return len(myStack) == 0