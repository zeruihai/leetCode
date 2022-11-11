####### My Solution #######
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        if l == 2:
            return min(height[0],height[1])

        right = l - 1
        left = 0
        tmp_area = min(height[left],height[right]) * right
        max_area = tmp_area
        count = 0

        while count != l-1:
            if  height[left] > height[right]:
                right -= 1   
            else:
                left += 1
            tmp_area = min(height[left],height[right]) * (right-left)
            if tmp_area > max_area:
                max_area = tmp_area
            count += 1

        return max_area