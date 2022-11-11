####### My Solution #######
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

        total = 0
        i = 0

        while i < len(s):
            if i!= len(s)-1 and roman[s[i]] < roman[s[i+1]]:
                total = total + roman[s[i+1]] - roman[s[i]]
                i += 2
            else:
                total += roman[s[i]]
                i+=1
        return total

####### Online Solution ####### 68%
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

        total = 0
        i = 0

        for i in range(0,len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]] 
            else:
                total += roman[s[i]]

        return total + roman[s[-1]]

####### Online Solution ####### 99.40%
class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0

        s = s.replace("IX","VIIII").replace("IV","IIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            total += translations[char]