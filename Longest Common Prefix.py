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