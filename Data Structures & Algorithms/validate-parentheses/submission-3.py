class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        myDict = {"{":"}", 
                "(": ")", 
                "[":"]"}
        i = 0
        if len(s) % 2 != 0 or s[0] not in myDict.keys() or s[len(s)-1] in myDict.keys():
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