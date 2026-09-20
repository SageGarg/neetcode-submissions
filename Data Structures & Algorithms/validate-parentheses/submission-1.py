class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        myDict = {"{":"}", 
                "(": ")", 
                "[":"]"}
        i = 0
        if len(s) % 2 != 0:
            return False
        for ch in s:
            if ch in myDict.keys():
                myStack.append(ch)
            else:
                for x,y in myDict.items():
                    if myStack[-1] ==x:
                        if ch == y:
                            myStack.pop()
                            break
                
            i += 1
    
           
        if (len(myStack) == 0):
            return True

        #print(myStack)
        
        
        return False