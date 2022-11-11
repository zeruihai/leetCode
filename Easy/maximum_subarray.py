####### My Solution ####### 88.3%

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]

        return max(nums)


### Divide and Conquer
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:


        def helper(nums,left,right):
            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0
            for i in range(mid,left,-1):
                curr += nums[i]
                best_left_sum = max(best_left_sum,curr)

            curr = 0

            for i in range(mid,right):
                curr += nums[i]
                best_right_sum = max(best_right_sum,curr)
            
            
            