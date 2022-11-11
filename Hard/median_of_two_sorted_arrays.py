class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        self.merge(nums1,m,nums2,n)
        sum = m + n
        med = sum // 2
        if sum % 2 == 0:
            
            res = (nums1[med] + nums1[med-1])/2
            return res
        
        else:
            res = nums1[med]
            return res

            

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
                elif nums2[0] >= nums1[-1]:
                    for i in range(len(nums2)):
                        nums1.insert(len(nums1),nums2[0])
                        nums2.pop(0)
                elif nums2[0] <= nums1[c1] or m == 0:
                    nums1.insert(c1,nums2[0])
                    nums2.pop(0)

                c1 += 1