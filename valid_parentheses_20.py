# Leet code problem 20. Valid Parentheses
# link:https://leetcode.com/problems/valid-parentheses/
# Jun 12, 2026

class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        d = {"(":["open",1],"[":["open",2],"{":["open",3],
            ")":["close",1],"]":["close",2],"}":["close",3],
            "":["invalid"],}
        for i,a in enumerate(s):
            b = s[i + 1] if i + 1 < len(s) else ""
            if "open" in d[a][0]:
                if "close" in d[b][0] and d[a][1] != d[b][1]:
                    temp.append(1)
                    break
                else:
                    temp.append(d[a])
            else:
                if ["open",d[a][1]] == (temp[-1] if temp else None):
                    temp.pop()
                else:
                    temp.append(1)
        if not temp:
            return True
        else:
            return False
