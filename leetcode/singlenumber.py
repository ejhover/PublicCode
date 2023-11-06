class Solution:
    def singleNumber(self, nums) -> int:
        nums.sort()
        left, right = 0, 1
        while left < right:
            try:
                if nums[left] == nums[right]:
                    left+=2
                    right+=2
                    continue
            except IndexError:
                return nums[left]
            if nums[left] != nums[right]:
                return nums[left]


j = Solution()
print(j.singleNumber([4, 1, 2, 1, 2, 4, 3]))
# [1, 1, 2, 2, 4]
