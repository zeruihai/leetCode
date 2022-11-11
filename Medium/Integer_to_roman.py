####### My Solution ####### 64.93%
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I",0:""}
        num_list = list(roman.keys())

        s = ""
        i = 0
        while num!= 0:
            if num >= 2 * num_list[i]:
                num -= num_list[i]
                s += roman[num_list[i]]
            if num >= num_list[i] and num < 2*num_list[i]:
                num -= num_list[i]
                s += roman[num_list[i]]
                i += 1
            if num < num_list[i]:
                i+= 1


        return s

####### Online Solution #######  96.65%
def intToRoman(self, num: int) -> str:
        roman = [(1000,"M"), (900,"CM"), (500,"D"), (400,"CD"), (100,"C"), (90,"XC"), (50,"L"), (40,"XL"), (10,"X"), (9,"IX"), (5,"V"), (4,"IV"), (1,"I")]

        str_list = []
        
        for value,symbol in roman:

            if num == 0:
                break
            count, num = divmod(num,value)

            str_list.append(count*symbol)

        return "".join(str_list)