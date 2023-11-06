# given array, return new array where each number is the product of the whole erray except for that value
import math
class Solution:
    def productExceptSelf(self, arr):
        ans = []
        for pos, i in enumerate(arr):
            p = 1*math.prod(arr[:pos]+arr[pos+1:])
            ans.append(p)
        return ans
p = Solution()
print(p.productExceptSelf([1, 2, 3, 4])) # [24, 12, 8, w6]