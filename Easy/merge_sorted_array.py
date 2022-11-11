from itertools import count


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        c1 = 0
        if n != 0:
            
            while nums2:
                if m == 0:
                    for i in range(n):
                        nums1.insert(i,nums2[0])
                        nums2.pop(0)
                elif nums2[0] >= nums1[-n-1]:
                    for i in range(len(nums2)):
                        nums1.insert(-n,nums2[0])
                        nums2.pop(0)
                elif nums2[0] <= nums1[c1] or m == 0:
                    nums1.insert(c1,nums2[0])
                    nums2.pop(0)

                c1 += 1

            for i in range(n):
                nums1.pop()
        
