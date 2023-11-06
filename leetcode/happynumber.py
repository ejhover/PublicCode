class Solution:
    def isHappy(self, n: int) -> bool:
        ans = set()
        while True:
            n = sum((int(i)**2 for i in str(n)))
            if len(str(n)) <= 1:
                if n == 1:
                    return True
                elif n in ans:
                    return False
            ans.add(n)
        
        
j = Solution()
print(j.isHappy(1111111))