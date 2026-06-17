# Leet Code problem 70. Climbing Stairs
# link:https://leetcode.com/problems/climbing-stairs/
# Jun 16, 2026

class Solution:
    def climbStairs(self, n: int) -> int:
        from math import factorial
        temp = []
        l = []
        perm_count = 0
        result = 0
        while not l or not all(b == 1 for b in l[-1]):
            a = temp.copy()
            while sum(a) < n:
                if sum(a) + 1 == n:
                    a.append(1)
                else:
                    a.append(2)
            a = sorted(a)
            if a not in l:
                l.append(a)
            temp.append(1)

        for e in l:
            a1 = e.count(1)
            a2 = e.count(2)
            perm_count = factorial(len(e)) // (factorial(a1) * factorial(a2))
            result += perm_count
        return result
