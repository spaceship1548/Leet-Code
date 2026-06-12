# Leet Code problem 14. Longest Common Prefix
# link:https://leetcode.com/problems/valid-parentheses/
# Jun 11, 2026

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(key=len)
        a = strs[0]
        prefix = ""
        for i,b in enumerate(a):
            if  all([b == c[i] for c in strs]):
                prefix = prefix + b
            else:
                break
        return prefix