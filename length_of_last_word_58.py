# Leet Code problem 58. Length of Last Word
# link:https://leetcode.com/problems/length-of-last-word/
# Jun 14, 2026

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
