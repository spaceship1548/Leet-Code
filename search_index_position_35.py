# Leet code problem 35. Search Insert Position
# link:https://leetcode.com/problems/search-insert-position/
# jun 29, 2026

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for a in nums:
                if a > target:
                    return nums.index(a)
            return len(nums)


