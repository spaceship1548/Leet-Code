# Leet Code problem 9. Palindrome Number
# link:https://leetcode.com/problems/palindrome-number/
# Jun 10, 2026

class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = str(x)
        a = 0
        b = -1
        while a < len(l):
            if l[a] != l[b]:
                return False
                break
            else:
                a = a + 1
                b = b - 1
        if a == len(l):
            return True



