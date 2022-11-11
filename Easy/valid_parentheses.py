from multiprocessing.synchronize import Lock
from pickle import TRUE
from queue import Empty

####### My Solution ####### 76.91%
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses= {"(":")","[":"]","{":"}"}
        if s[0] in parentheses.values():
            return False
        for i in range(0,len(s)):

            try:
                if s[i] in parentheses:
                    stack.insert(0,s[i])
                elif s[i] == parentheses[stack[0]]:
                    stack.pop(0)
                else:
                    return False
            except IndexError:
                return False
        if stack:
            return False
        else: 
            return True

