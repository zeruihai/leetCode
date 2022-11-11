
####### My Solution ####### 5%

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = [None]*len(nums)
        for i in range(0,len(nums)):

            if nums[i] in x:
                x[i] = '_'
            else:
                x[i] = nums[i]
            
        for j in range(len(nums)-1,-1,-1):
            if x[j] == '_':
                nums.pop(j)
        

        return len(nums)




####### Online Solution ####### 51%

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 1
        for i in range(len(nums)-1):
            if(nums[i]!=nums[i+1]):
                nums[x] = nums[i+1]
                x+=1
        return(x)