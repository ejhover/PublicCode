class Solution:
    def lcp(self, str1, str2):
        p = ""
        try:
            for pos, i in enumerate(str1):
                if "".join(str1[:pos+1]) == str2[:pos+1]:
                    p = "".join(str1[:pos+1])
            return p
        except:
            return ""
    def longestCommonPrefix(self, strs) -> str:
        try:
            q = self.lcp(strs[0],strs[1])
        except:
            return strs[0]
        for i in (strs[2:]):
            q = self.lcp(q,i)
        return q if q else ""

p = Solution()
print(p.longestCommonPrefix(["flower","flower","flow","flowe"]))