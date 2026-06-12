# Leet code problem 13. Roman to Integer
# link:https://leetcode.com/problems/roman-to-integer/
# jun 10, 2026

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,
        "IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900,}
        l = ["I","X","C"]
        value = 0
        a = 0
        b = 1
        while a < len(s):
            if b < len(s):
                if s[a] in l and s[a] + s[b] in d:
                    value += d[s[a] + s[b]]
                    a += 1
                    b += 1
                else:
                    value += d[s[a]]
            else:
                value += d[s[a]]
            b += 1
            a += 1
        return value