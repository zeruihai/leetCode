from pickle import LIST
from typing import List

from pip import main
hashmap = {}

####### My Solution #######
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range (len(nums)):
            hashmap[nums[i]] = i
            
        for i in range (len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i,hashmap[complement]]
            
            

Solution.twoSum(Solution,[6,3,9,2,4],6)
print(hashmap)