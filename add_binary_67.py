# Leet Code problem 67. Add Binary
# link:https://leetcode.com/problems/add-binary/
# jun 15, 2026

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)
        return bin(a+b)[2:]