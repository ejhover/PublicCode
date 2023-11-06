'''class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        for i, n in enumerate(nums):
            if i != 0:
                try:
                    if n == nums[i-1]:
                        continue
                except:
                    pass
            target = 0-n
            low = i+1
            high = len(nums)-1
            while low < high:
                if nums[low] + nums[high] > target:
                    high-=1
                elif nums[low] + nums[high] < target:
                    low+=1
                elif nums[low] + nums[high] == target:
                    if [n, nums[low], nums[high]] in ans:
                        low+=1
                        high-=1
                    else:
                        ans.append([n, nums[low], nums[high]])
                        low+=1
                        high-=1
        return ans'''
# num1 + num2 + num3 = 0
                   # 1+-4 == 1 
# [-4, -1, -1, 0, 1, 2]
# [-1, -1, 2], [-1, 0, 1]
# -1 + num2 + num3 = 0
class Solution:
    def threeSum(self, nums):
        nums.sort()
        d = {}
        ans = []
        for i1, n1 in enumerate(nums):
            for i2, n2 in enumerate(nums[i1+1:]):
                target = 0-n1
                if i1 != 0:
                    if n2 == n1:
                        continue
                if target-n2 in d and d[target-n2] not in [i1, i2+i1+1]:
                    if sorted([n1, n2, target-n2]) in ans:
                        continue
                    else:
                        ans.append(sorted([n1, n2, target-n2]))
                else:
                    d[n2] = i2+i1+1
        return ans
                

p = Solution()
print(p.threeSum([1,2,-2,-1]))