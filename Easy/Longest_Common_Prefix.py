####### My Solution ####### 36.66%
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_len = len(min(strs,key=len))
        temp = [""]*len(strs)
        s = ""
        for i in range(0,shortest_len):
            for j in range(0,len(strs)):
                temp[j] += strs[j][i]
            
            if all(ele == temp[0] for ele in temp) == False:
                return s
            s += strs[j][i]

        return s      


        

####### Online Solution ####### 78.25% 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 

####### Online Solution ####### 48.80%
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
                #since list of string will be sorted and retrieved min max by alphebetic order
        s1 = min(strs)
        s2 = max(strs)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i] #stop until hit the split index
        return s1

####### Online Solution ####### 79.21% 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        m, M, i = min(strs), max(strs), 0
        for i in range(min(len(m),len(M))):
            if m[i] != M[i]: break
        else: i += 1
        return m[:i]