####### My Solution #######
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0
        flag = False
        if x < 0:
            x = abs(x)
            flag = True
        while x % 10 == 0:
            x = x // 10
        
        if x < 10:
            if flag == True:
                return -x
            else:
                return x
        
        l1 = []
        while x // 10 != 0:
            l1.append(str(x%10))
            x = x // 10

        l1.append(str(x))

        if flag == True:
            res = int("".join(l1)) * -1
        else:
            res = int("".join(l1))
        if res < - 2 ** 31 or res > 2 ** 31 -1: return 0
        return res

####### Online Solution #######
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0
    
        if x < 0:
            x = abs(x)
            symbol = -1
        else:
            symbol = 1

        while x % 10 == 0:
            x = x // 10
        
        if x < 10:
            return x * symbol
        res = 0
        while x // 10 != 0:
            res = res * 10 + x % 10
            x = x // 10

        res = res * 10 + x

        if res < - 2 ** 31 or res > 2 ** 31 -1: return 0
        return res * symbol