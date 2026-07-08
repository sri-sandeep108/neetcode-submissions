class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in hash_set:
                length = 1
                while (n+length) in hash_set:
                    length += 1
                longest = max(length, longest)
        return longest
            