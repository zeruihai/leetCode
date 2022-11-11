####### My Solution ####### 61.82%

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pos = 0
        for i in range(0,len(nums)):
            if target > nums[i]:
                
                pos += 1 
            if nums[i] == target:
                return i
        
        return pos