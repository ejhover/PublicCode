class Solution:
    def isValid(self, s: str):
        if ((len(s)%2) != 0):
            return False
        start = ["(", "{", "["]
        end = [")", "}", "]"]
        curr = []
        for i in start:
            if s.count(i) != s.count(end[start.index(i)]):
                return False
        for pos, i in enumerate(s):
            if i in start:
               curr.append(i)
            if i in end:
                if not curr:
                    return False
                if (start[end.index(i)] == curr.pop()):
                    continue
                else:
                    return False
        return True
p = Solution()

print(p.isValid("(){}}{"))