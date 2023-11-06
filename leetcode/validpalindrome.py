class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(i for i in s.strip().lower() if i.isalnum())
        return s == s[::-1]