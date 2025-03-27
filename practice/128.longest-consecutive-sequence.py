# @leet start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0
        for n in nums:
            if n-1 not in hashset:
                longest = 0
                while (n+longest) in hashset:
                    longest += 1

                res = max(longest, res)

        return res
# @leet end 
