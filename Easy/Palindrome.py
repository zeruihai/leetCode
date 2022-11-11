####### My Solution #######
def get_digit(number, n):
            return number // 10**n % 10
class Solution:
    
        
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        digits = len(str(x)) // 2
        temp = len(str(x))-1
        
        for i in range(0,digits):
            if get_digit(x,i) != get_digit(x,temp):
                return False
            temp -= 1
        
        return True