class Solution:
    def plusOne(self, digits):
        ans = 0
        for pos, i in enumerate(digits):
            ans += i*(10**(len(digits)-pos-1))
        return list(str(ans+1))
p = Solution()
print(p.plusOne([9, 9, 9, 9]))