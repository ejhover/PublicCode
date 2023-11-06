class Solution:
    def fibonacci(self, n):
        a = 0
        b = 1
        for _ in range(n):
            a, b = b, a + b
        return a
# DISPLAYS THE DIFFERENCE IN EFFICIENCY FROM RECURSION RATHER THAN THIS MORE CLEVER WAY ALSO RELATING TO CLIMBSTAIRS PROBLEM
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
p = Solution()

print(p.fibonacci(2))
print(fib(2))