class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        l = []
        if length < 3:
            return l
        nums.sort()
        index = 0
        left = 1
        right = length - 1
        checklist = []
        indexlist = {}
        while left<right:
            if nums[index] in indexlist and indexlist[nums[index]] != index:
                index += 1
                right = length - 1
                left = index + 1
            elif nums[index] + nums[left] + nums[right]<0:
                if right - left > 1:
                    left += 1
                else:
                    index += 1
                    right = length - 1
                    left = index + 1
            elif nums[index] + nums[left] + nums[right]>0:
                if right - left > 1:
                    right -= 1
                else:
                    index += 1
                    right = length - 1
                    left = index + 1
            else:
                bracket = [nums[left] , nums[right] , nums[index]]
                if set(bracket) not in checklist:
                    l.append(bracket)
                    checklist.append(set(bracket))
                    indexlist[nums[index]] = index
                if right - left > 2:
                    right -= 1
                    left += 1
                else:
                    index += 1
                    right = length - 1
                    left = index + 1
                
        return l


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1