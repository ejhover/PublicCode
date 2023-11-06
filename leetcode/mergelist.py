class Solution:
    def merge(self, nums1, m, nums2, n):
        for pos, i in enumerate(nums1):
            if not nums2:
                break
            if not nums1:
                nums1 = nums1+nums2
            
        print(nums1)
p = Solution()
p.merge([1,2,3,0,0,0], 3, [2,5,6], 3)